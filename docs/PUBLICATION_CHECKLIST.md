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
- [ ] Verify any additional branches/tags and run a dedicated full-history secret scanner; manual pattern matching is not sufficient.
- [ ] Run a dedicated secret scanner on the full Git history, not only current files.
- [x] Confirm pytest, dependency audit, Bandit, and detect-secrets checks passed in GitHub Actions run #21 (commit `f7e33cf`); current-file scanner does not cover historical versions.
- [ ] Confirm Meta and SQL credentials previously used in development have not been exposed; rotate any exposed credentials.
- [ ] Verify the demonstration using disposable accounts and a test database; static checks do not establish runtime correctness.
- [ ] Decide license only after confirming intellectual property ownership and publication authorization.
- [ ] Review GitHub Actions and repository settings again after any visibility change.
- [ ] Obtain explicit approval from repository owner before switching to public.

## Limitations
CodeQL was removed from the workflow because results could not be uploaded from this private repository. This is not a passed CodeQL analysis. Bandit and pip-audit do not guarantee that source code or history is free of secrets or vulnerabilities.
