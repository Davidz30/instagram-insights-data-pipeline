"""Import media metadata and engagement metrics from Instagram Graph API."""
from datetime import datetime, timezone

from common import MetaClient, active_accounts, sql_connect, utc_now_naive


FIELDS = "id,media_type,media_product_type,timestamp,like_count,comments_count"
METRICS = ("reach", "saved", "shares", "total_interactions")


def as_number(item):
    if "total_value" in item:
        return item["total_value"].get("value")
    values = item.get("values") or []
    return values[-1].get("value") if values else None


def media_insights(client, media_id, media_type):
    if media_type == "STORY":
        return {}
    try:
        payload = client.get(f"/{media_id}/insights", {"metric": ",".join(METRICS)})
        return {entry["name"]: as_number(entry) for entry in payload.get("data", [])}
    except RuntimeError:
        # Some metrics are unavailable for certain media types.
        return {}


def fetch_media(client, account_id):
    params = {"fields": FIELDS, "limit": 100}
    after = None
    seen = set()
    while True:
        if after:
            params["after"] = after
        payload = client.get(f"/{account_id}/media", params)
        for item in payload.get("data", []):
            if item.get("id") and item["id"] not in seen:
                seen.add(item["id"])
                yield item
        # Use the cursor, never the full paging URL (which can carry secrets).
        after = (payload.get("paging", {}).get("cursors") or {}).get("after")
        if not after or not payload.get("paging", {}).get("next"):
            break


def save_media(cursor, account_id, media, metrics):
    published = datetime.fromisoformat(media["timestamp"].replace("Z", "+00:00"))
    published = published.astimezone(timezone.utc).replace(tzinfo=None)
    values = (
        str(media["id"]), account_id, published,
        media.get("media_type"), media.get("media_product_type"),
        media.get("like_count"), media.get("comments_count"),
        metrics.get("reach"), metrics.get("saved"), metrics.get("shares"),
        metrics.get("total_interactions"), utc_now_naive(),
    )
    cursor.execute("""
        UPDATE dbo.f_instagram_midias SET
            DTA_PUBLICACAO=?, MEDIA_TYPE=?, MEDIA_PRODUCT_TYPE=?,
            LIKE_COUNT=?, COMMENTS_COUNT=?, REACH=?, SAVED=?, SHARES=?,
            TOTAL_INTERACTIONS=?, DTA_CARGA=?
        WHERE MEDIA_ID=? AND INSTAGRAM_ID=?
    """, *(values[2:] + values[:2]))
    if cursor.rowcount == 0:
        cursor.execute("""
            INSERT INTO dbo.f_instagram_midias
            (MEDIA_ID, INSTAGRAM_ID, DTA_PUBLICACAO, MEDIA_TYPE,
             MEDIA_PRODUCT_TYPE, LIKE_COUNT, COMMENTS_COUNT, REACH,
             SAVED, SHARES, TOTAL_INTERACTIONS, DTA_CARGA)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, *values)


def main():
    client = MetaClient()
    with sql_connect() as connection:
        for account_id in active_accounts(connection):
            try:
                cursor = connection.cursor()
                for media in fetch_media(client, account_id):
                    metrics = media_insights(client, str(media["id"]), media.get("media_type"))
                    save_media(cursor, account_id, media, metrics)
                connection.commit()
                print("Media import completed for one account")
            except Exception:
                connection.rollback()
                print("Media import failed for one account; details suppressed")
                raise


if __name__ == "__main__":
    main()
