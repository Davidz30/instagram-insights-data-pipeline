"""Shared configuration, Meta API client and SQL connection utilities."""
import os
import time
from datetime import datetime, timezone

import pyodbc
import requests


def required_env(name: str) -> str:
    value = os.getenv(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def sql_connect():
    """Keep the complete connection string in a secret store or environment."""
    return pyodbc.connect(required_env("SQL_CONNECTION_STRING"), timeout=15)


class MetaClient:
    def __init__(self):
        self.token = required_env("META_ACCESS_TOKEN")
        self.version = os.getenv("META_API_VERSION", "v26.0")
        if not self.version.startswith("v") or not self.version[1:].replace(".", "").isdigit():
            raise ValueError("Invalid META_API_VERSION")
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.token}"})

    def get(self, path: str, params: dict | None = None) -> dict:
        """Never log URLs, API bodies or account identifiers."""
        if not path.startswith("/") or "://" in path:
            raise ValueError("Only relative Graph API paths are allowed")
        url = f"https://graph.facebook.com/{self.version}{path}"
        for attempt in range(3):
            try:
                response = self.session.get(url, params=params, timeout=30)
                if response.status_code in (429, 500, 502, 503, 504) and attempt < 2:
                    time.sleep(2 ** attempt)
                    continue
                response.raise_for_status()
                return response.json()
            except requests.RequestException:
                if attempt == 2:
                    raise RuntimeError("Meta API request failed; details withheld to protect secrets") from None
                time.sleep(2 ** attempt)
        raise RuntimeError("Meta API request failed")


def active_accounts(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT INSTAGRAM_ID FROM dbo.d_instagram_contas WHERE ATIVO = 1")
    return [str(row[0]) for row in cursor.fetchall()]


def utc_now_naive():
    return datetime.now(timezone.utc).replace(tzinfo=None)
