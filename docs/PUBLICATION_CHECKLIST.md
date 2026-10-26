# Checklist before changing repository visibility

Status: **NOT APPROVED FOR PUBLIC RELEASE**.

## Completed
- [x] Repository contains only a standalone demonstration.
- [x] Current tracked files reviewed for known internal IP, SQL login, database name, organization name and real Instagram handle.
- [x] Placeholder-only `.env.example`.
- [x] GitHub Actions syntax, pip-audit and Bandit passed on commit `7a976a3`.

## Required before publication
- [x] Repository owner stated that company authorization to publish exists (not independently verified).
- [x] Manually inspect 25 available commits for known internal identifiers (no matches found).
- [x] GitHub branch search returned only `main` at time of review.
- [ ] Verify whether tags or other refs exist before publication.
- [x] Gitleaks full-history scan passed (manual GitHub Actions run #1, commit `84f4dc1`); no leaks detected by configured rules.
- [x] Confirm pytest, dependency audit, Bandit, and detect-secrets checks passed in GitHub Actions run #21 (commit `f7e33cf`); current-file scanner does not cover historical versions.
- [ ] Confirm Meta and SQL credentials previously used in development have not been exposed; rotate any exposed credentials.
- [x] Repository owner elected to skip end-to-end testing of the independent demo. The original production implementation was reportedly tested, but the published demo has **not** been functionally validated; disclose this limitation in README.
- [ ] Decide license only after confirming intellectual property ownership and publication authorization.
- [ ] Review GitHub Actions and repository settings again after any visibility change.
- [ ] Obtain explicit approval from repository owner before switching to public.

## Limitations
CodeQL was removed from the workflow because results could not be uploaded from this private repository. This is not a passed CodeQL analysis. Bandit and pip-audit do not guarantee that source code or history is free of secrets or vulnerabilities.
