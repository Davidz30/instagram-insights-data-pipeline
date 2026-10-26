# Operations

Schedule the media and account scripts independently using your approved scheduler.
Use a non-admin SQL identity with narrowly scoped permissions and encrypted SQL connections.
Monitor success/failure without logging API responses, token-bearing URLs, or account identifiers.
Use staging tables or transaction-safe upserts for concurrent workloads.
Backfill and rate-limit strategy should be defined before production deployment.
