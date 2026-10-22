# Contributing to QBF Consulting repositories

QBF repositories use pull requests, repository-specific validation, and contribution provenance appropriate to the repository.

## Developer Certificate of Origin (DCO)

Human-authored commits to governed QBF repositories must carry a DCO sign-off trailer:

```text
Signed-off-by: Your Name <your@email.example>
```

Create a signed-off commit with:

```bash
git commit -s -m "type(scope): describe the change"
```

If only the latest local commit is missing the trailer:

```bash
git commit --amend --signoff --no-edit
```

For a local series that must be repaired, use an appropriate interactive rebase or `git rebase --signoff <base>`, then verify the rewritten history before force-pushing the topic branch.

A DCO sign-off certifies the contribution. It is separate from cryptographic commit signing and from pull-request approval.

GitHub web commits are covered by QBF's organization setting requiring web-based commit sign-off. Automated commits made by authenticated GitHub Apps/bots are not given manufactured human sign-offs; the DCO workflow records them as automation and preserves their bot provenance.

Repository-specific `CONTRIBUTING.md` files may add requirements. They remain authoritative for additional validation, compatibility, licensing, or review obligations.

## Before merge

A governed repository should require its applicable DCO and CI checks before merge. Do not weaken or bypass a failed check merely to obtain a green pull request.


