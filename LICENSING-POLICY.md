# QBF Consulting Portfolio Licensing Policy

Status: Organization governance policy  
Scope: Public repositories stewarded by QBF Consulting LLP  
Authority: Repository-local licensing remains authoritative for each repository  
Effective from: 2026-09-28

## Purpose

QBF publishes specifications, governance models, documentation, schemas, software, tests, validators, workflows, evidence artifacts, and other open knowledge. These artifact classes do not always have the same licensing requirements. QBF therefore uses an artifact-sensitive licensing model rather than imposing one license on every repository.

The objective is to make reuse permissions explicit, preserve third-party provenance, support implementation and interoperability, and avoid accidental relicensing.

## Default licensing rules

### Executable and machine-actionable artifacts: Apache-2.0

Unless repository-local provenance or an explicit exception requires otherwise, source code, reference implementations, scripts, validators, conformance tooling, tests, machine-readable schemas and contracts, executable configuration, workflows, automation, and implementation evidence artifacts SHOULD use Apache-2.0.

### Specifications, frameworks, and broadly reusable documentation: CC BY 4.0

Unless an explicit exception applies, normative and informative specification text, reference frameworks, explanatory documentation, diagrams, narrative examples, implementation guidance, governance prose, and release notes SHOULD use CC BY 4.0.

### Reciprocal knowledge commons: CC BY-SA 4.0 by deliberate exception

CC BY-SA 4.0 MAY be used where maintaining a reciprocal open knowledge commons is an explicit project objective. ShareAlike is not the default for QBF specifications. A repository using it SHOULD record why reciprocity is materially important.

### NonCommercial restrictions

CC BY-NC-SA and other NonCommercial licenses SHOULD NOT be used for new QBF open technical infrastructure unless a specific documented intellectual-property objective requires the restriction.

## Provenance overrides defaults

Existing third-party or upstream licensing obligations take precedence over QBF defaults. A fork, transferred repository, derived work, or repository containing third-party material MUST preserve applicable copyright, attribution, notice, and license obligations.

QBF stewardship does not imply authority to relicense upstream material. Where inherited licensing differs from QBF defaults: retain the inherited license where required; document provenance and current stewardship; license sufficiently separable new QBF-authored artifacts independently only where QBF has authority to do so; and avoid creating an ambiguous repository-wide claim.

trust-infrastructure-schemas, for example, retains upstream MIT licensing because its provenance is a QBF-stewarded fork of archetech/schemas.

## Mixed-content repositories

A repository containing materially different artifact classes SHOULD publish a licensing map. Preferred files are LICENSE, LICENSE-CONTENT, LICENSE-CODE, and an optional machine-readable artifact-license policy.

| Artifact class | Default license |
|---|---|
| Specification and documentation | CC BY 4.0 |
| Software and source code | Apache-2.0 |
| Schemas and executable contracts | Apache-2.0 |
| Validators and tests | Apache-2.0 |
| Automation and workflows | Apache-2.0 |
| Reciprocal knowledge material | CC BY-SA 4.0 only when explicitly declared |
| Third-party material | Applicable third-party license |

Repository-local files MAY define more precise rules and always govern their own scope.

## Existing QBF exceptions

- trust-infrastructure-schemas — MIT retained because of upstream provenance.
- trust-systems-meta-model — CC BY-SA 4.0 retained for the current candidate semantic commons.
- governance-authority-assurance-metamodel — CC BY 4.0 retained for the current specification baseline.
- open-national-digital-trust-framework — CC BY 4.0 retained as the framework-content license.
- agent-registry-protocol — mixed CC BY 4.0 / Apache-2.0 artifact licensing map.
- digital-trust-failure-corpus — mixed CC BY 4.0 / Apache-2.0 artifact licensing map.

These exceptions are not precedent for arbitrary divergence. New deviations SHOULD record a provenance or governance justification.

## Authority and scope

This organization policy establishes QBF defaults. It does not itself relicense repository content.

For any artifact, authority is determined in this order: file-specific license or SPDX declaration; repository-local licensing map; repository root license declaration; then this organization default only for new QBF-authored material where no stronger obligation exists.

Absence of a license is not interpreted as permission.

## Changes to licensing

A repository license change is a consequential governance change. A proposed change SHOULD identify licensing authority, third-party and historical contributions, prospective versus retroactive effects, compatibility and redistribution impact, and preserve the Issue → PR → review → merge judgment trail.

No automated portfolio process may silently rewrite repository licenses.

## Machine-verifiable portfolio control

The QBF .github repository publishes a licensing audit that checks public QBF repositories for an explicit licensing declaration. The audit verifies declaration and recognized policy state; it does not provide legal interpretation. Missing or unrecognized licensing remains a failing condition.

## Governing question

> Who has authority to grant which reuse rights over which artifact, and is that boundary explicit to a downstream adopter?
