# Checklist before changing repository visibility

Status: **NOT APPROVED FOR PUBLIC RELEASE**.

## Completed
- [x] Repository contains only a standalone demonstration.
- [x] Current tracked files reviewed for known internal IP, SQL login, database name, organization name and real Instagram handle.
- [x] Placeholder-only `.env.example`.
- [x] GitHub Actions syntax, pip-audit and Bandit passed on commit `7a976a3`.

## Required before publication
- [ ] Obtain written permission from the relevant rights holder to publish code derived from work projects.
- [ ] Review all commit history and any branches/tags for secrets and internal information.
- [ ] Run a dedicated secret scanner on the full Git history, not only current files.
- [ ] Confirm the new pytest and detect-secrets GitHub Actions run passes (commit `35482b5`); the new scanner currently checks tracked files, not all historical versions.
- [ ] Confirm Meta and SQL credentials previously used in development have not been exposed; rotate any exposed credentials.
- [ ] Verify the demonstration using disposable accounts and a test database; static checks do not establish runtime correctness.
- [ ] Decide license only after confirming intellectual property ownership and publication authorization.
- [ ] Review GitHub Actions and repository settings again after any visibility change.
- [ ] Obtain explicit approval from repository owner before switching to public.

## Limitations
CodeQL was removed from the workflow because results could not be uploaded from this private repository. This is not a passed CodeQL analysis. Bandit and pip-audit do not guarantee that source code or history is free of secrets or vulnerabilities.
