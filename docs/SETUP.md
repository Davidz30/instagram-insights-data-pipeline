# Local setup

1. Install Python 3.12, Microsoft ODBC Driver 18 for SQL Server, and create a virtual environment.
2. Install dependencies: `python -m pip install -r requirements.txt`.
3. Copy `.env.example` to `.env`, replacing examples locally; never commit `.env`.
4. Export `META_ACCESS_TOKEN` and `SQL_CONNECTION_STRING` as environment variables.
5. Apply `sql/01_schema.sql` then `sql/02_views.sql` to a disposable database.
6. Register test Instagram professional account IDs in the local database.
7. Run `python src/carga_instagram_midias.py` and `python src/carga_insights_conta.py`.

Note: The scripts intentionally do not load `.env` automatically. Supply variables
through your process manager or secret store. `.env.example` is documentation only.

This is a demonstration, not a production-ready integration. Verify API responses,
pagination, rate limits, permissions and database behavior in your own environment.
