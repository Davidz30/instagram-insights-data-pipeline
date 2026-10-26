# Architecture

Meta Instagram Graph API (professional account) → Python ETL → SQL Server → Power BI.

The two independent jobs extract account-level daily metrics and media-level metrics.
A SQL Server Agent schedule can run the Python modules on an approved host.

All connection configuration is external. Access tokens must be scoped to required
permissions and rotated regularly. Database identity needs only read on the account
registry and appropriate write access to the two destination tables.

This repository is an independent demonstration and does not reproduce corporate
infrastructure or real Instagram accounts. Validate API permissions and metric
availability for the selected API version before deployment.
