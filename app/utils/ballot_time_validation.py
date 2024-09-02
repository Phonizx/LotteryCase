from datetime import datetime, timedelta, timezone


def is_before_midnight() -> bool:
    """returns True if the current time is before 5 minutes midnight otherwise False"""
    dt_now = datetime.now(timezone.utc)
    today_midnight = datetime.combine(dt_now, datetime.max.time(), tzinfo=timezone.utc) - timedelta(minutes=4)
    if dt_now < today_midnight:
        return True
    return False
