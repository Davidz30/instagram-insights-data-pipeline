"""Import previous-day account insights from Instagram Graph API."""
from datetime import datetime, timedelta, timezone

from common import MetaClient, active_accounts, sql_connect, utc_now_naive


def metric_value(item):
    if "total_value" in item:
        return item["total_value"].get("value")
    values = item.get("values") or []
    return values[-1].get("value") if values else None


def account_insights(client, account_id, start, end):
    result = {}
    for metric in ("reach", "profile_views", "accounts_engaged"):
        try:
            payload = client.get(f"/{account_id}/insights", {
                "metric": metric,
                "period": "day",
                "metric_type": "total_value",
                "since": int(start.timestamp()),
                "until": int(end.timestamp()),
            })
            for item in payload.get("data", []):
                result[item.get("name", metric)] = metric_value(item)
        except RuntimeError:
            # Availability depends on account type, permission and API version.
            result[metric] = None
    return result


def save_account(cursor, account_id, start, end, profile, metrics):
    data = (
        profile.get("followers_count"), profile.get("media_count"),
        metrics.get("reach"), metrics.get("profile_views"),
        metrics.get("accounts_engaged"), utc_now_naive(),
    )
    key = (account_id, start.date(), (end - timedelta(days=1)).date())
    cursor.execute("""
        UPDATE dbo.f_instagram_insights_conta SET
          FOLLOWERS_COUNT=?, MEDIA_COUNT=?, REACH=?,
          PROFILE_VIEWS=?, ACCOUNTS_ENGAGED=?, DTA_CARGA=?
        WHERE INSTAGRAM_ID=? AND DTA_INICIO=? AND DTA_FIM=?
    """, *(data + key))
    if cursor.rowcount == 0:
        cursor.execute("""
            INSERT INTO dbo.f_instagram_insights_conta
            (INSTAGRAM_ID, DTA_INICIO, DTA_FIM, FOLLOWERS_COUNT,
             MEDIA_COUNT, REACH, PROFILE_VIEWS, ACCOUNTS_ENGAGED, DTA_CARGA)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, *(key + data))


def main():
    client = MetaClient()
    end = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    start = end - timedelta(days=1)
    with sql_connect() as connection:
        for account_id in active_accounts(connection):
            try:
                profile = client.get(f"/{account_id}", {
                    "fields": "id,followers_count,media_count"
                })
                insights = account_insights(client, account_id, start, end)
                save_account(connection.cursor(), account_id, start, end, profile, insights)
                connection.commit()
                print("Account insights imported for one account")
            except Exception:
                connection.rollback()
                print("Account insights import failed for one account; details suppressed")
                raise


if __name__ == "__main__":
    main()
