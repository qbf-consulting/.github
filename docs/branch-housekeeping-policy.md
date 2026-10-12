# Branch housekeeping policy v1.0

**Authority:** repository's default branch, GitHub branch protections, open pull requests and explicit exemptions. This workflow is advisory in dry-run and mutating only when enabled by the caller.

**Invariant:** Automatically delete only when *complete integration* into the current default branch is positively established. Inactivity, age, naming, or a closed-unmerged PR never establish eligibility.

## Evidence accepted
1. The candidate HEAD is an ancestor of the current default HEAD (GitHub compare reports zero commits ahead).
2. A closed and merged PR originates from this repository, targets the current default branch, and its recorded head SHA exactly equals the current branch HEAD; its merge commit is an ancestor of the current default HEAD. This supports squash/rebase histories without accepting arbitrary patch equivalence.

## Mandatory retention
Default or protected branches, branches with open PRs, and deployment/long-running namespace exclusions. Defaults include `gh-pages`, `develop`, `release/**`, `research/**`, `draft/**`, `convergence/**`, and related operational prefixes. Callers may extend the exclusions.

Missing API evidence, exceptions, or changed SHA during revalidation => **RETAIN**. No age threshold is used. All candidate dispositions appear in the workflow job summary.

## Security and known limitations
The reusable job receives only the invoking repository's scoped `GITHUB_TOKEN` with `contents: write` and `pull-requests: read`. Use only for repositories under authorized control. The GitHub branch DELETE REST endpoint is not conditional on an expected SHA: a very small update-versus-delete race remains after final revalidation. Repository branch protections and rulesets should enforce any additional critical preservation controls. An authorized write may be denied by a ruleset; the report records that refusal as retained. GitHub Actions cron timing is best-effort, not an exact-time guarantee.

## Rollout
Call from a repository-local scheduled workflow; start with `dry_run: true`. Review job summaries and enable `dry_run: false` only for repos whose protected deployment/work branches are accounted for. Scheduled workflows run only from the default branch; GitHub may disable schedules in inactive public repos.

## Manual recovery
A deleted branch ref can be recreated from its audit-recorded SHA while the commit remains available. Deletion does not remove commits, tags, or releases immediately. Consult the run summary before attempting recovery.
