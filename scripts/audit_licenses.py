#!/usr/bin/env python3
"""Fail-closed licensing declaration audit for public QBF repositories."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

ORG = os.environ.get("QBF_ORG", "qbf-consulting")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
POLICY_PATH = Path("licensing/portfolio-policy.json")
SELF_REPO = f"{ORG}/.github"


def request(url: str, accept: str = "application/vnd.github+json") -> urllib.request.Request:
    headers = {"Accept": accept, "X-GitHub-Api-Version": "2022-11-28"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    return urllib.request.Request(url, headers=headers)


def get_json(url: str):
    with urllib.request.urlopen(request(url), timeout=30) as response:
        return json.loads(response.read().decode("utf-8"))


def get_remote_text(repo: str, path: str) -> str | None:
    url = f"https://api.github.com/repos/{repo}/contents/{path}"
    try:
        with urllib.request.urlopen(request(url, "application/vnd.github.raw+json"), timeout=30) as response:
            return response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        raise


def get_text(repo: str, path: str) -> str | None:
    if repo == SELF_REPO:
        local = Path(path)
        if local.is_file():
            return local.read_text(encoding="utf-8")
    return get_remote_text(repo, path)


def classify(text: str) -> str:
    value = text.lower()
    has_apache = "apache license" in value and ("version 2.0" in value or "apache-2.0" in value)
    has_cc = "creative commons" in value or "cc by" in value or "cc-by" in value
    if "licensing map" in value and has_apache and has_cc:
        return "MIXED"
    if "attribution-sharealike 4.0" in value or "cc by-sa 4.0" in value or "cc-by-sa-4.0" in value:
        return "CC-BY-SA-4.0"
    if "attribution 4.0" in value or "cc by 4.0" in value or "cc-by-4.0" in value:
        return "CC-BY-4.0"
    if has_apache:
        return "Apache-2.0"
    if "mit license" in value:
        return "MIT"
    return "UNRECOGNIZED"


def list_public_repositories() -> list[dict]:
    repos: list[dict] = []
    page = 1
    while True:
        batch = get_json(f"https://api.github.com/orgs/{ORG}/repos?type=public&per_page=100&page={page}")
        if not batch:
            break
        repos.extend(batch)
        page += 1
    return sorted((r for r in repos if not r.get("archived", False)), key=lambda r: r["full_name"].lower())


def main() -> int:
    policy = json.loads(POLICY_PATH.read_text(encoding="utf-8"))
    recognized = set(policy["recognized_license_families"])
    declaration_paths = policy["declaration_paths"]
    mixed_markers = policy["mixed_map_markers"]
    exceptions = policy.get("exceptions", {})

    failures: list[str] = []
    rows: list[tuple[str, str, str, str]] = []

    for repo_info in list_public_repositories():
        repo = repo_info["full_name"]
        declaration_path = ""
        declaration_text = None
        for path in declaration_paths:
            declaration_text = get_text(repo, path)
            if declaration_text is not None:
                declaration_path = path
                break

        detected = "MISSING"
        if declaration_text is not None:
            detected = classify(declaration_text)
        else:
            marker_presence = [get_text(repo, marker) is not None for marker in mixed_markers]
            if all(marker_presence):
                detected = "MIXED"
                declaration_path = "+".join(mixed_markers)

        basis = "default/declaration"
        exception = exceptions.get(repo)
        if exception:
            basis = exception.get("basis", "declared-exception")
            expected = exception.get("license")
            if expected and detected != expected:
                failures.append(f"{repo}: expected exception license {expected}, detected {detected}")

        if detected == "MISSING":
            failures.append(f"{repo}: no explicit licensing declaration found")
        elif detected == "UNRECOGNIZED":
            failures.append(f"{repo}: licensing declaration at {declaration_path} is not recognized by policy")
        elif detected not in recognized:
            failures.append(f"{repo}: detected license {detected} is outside recognized policy families")

        rows.append((repo, detected, declaration_path or "—", basis))

    print("Repository licensing audit")
    print("===========================")
    for repo, detected, path, basis in rows:
        print(f"{repo}: {detected} [{path}] ({basis})")

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a", encoding="utf-8") as summary:
            summary.write("## QBF repository licensing audit\n\n")
            summary.write("| Repository | Detected | Declaration | Basis |\n")
            summary.write("|---|---|---|---|\n")
            for repo, detected, path, basis in rows:
                summary.write(f"| {repo} | {detected} | {path} | {basis} |\n")
            if failures:
                summary.write("\n### Failures\n\n")
                for failure in failures:
                    summary.write(f"- {failure}\n")

    if failures:
        print("\nFAILURES:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(f"\nPASS: {len(rows)} public non-archived QBF repositories have explicit recognized licensing.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
