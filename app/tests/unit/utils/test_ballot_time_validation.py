from datetime import datetime, timezone

import pytest
from freezegun import freeze_time

import app.utils as utilities


@pytest.mark.asyncio
async def test_is_before_midnight_happy_flow():
    with freeze_time("2024-07-25 12:24"):
        assert utilities.is_before_midnight() is True


@pytest.mark.asyncio
async def test_is_before_midnight_sad_flow():
    midnignt = str(datetime.combine(datetime.now(), datetime.max.time(), tzinfo=timezone.utc))
    with freeze_time(midnignt):
        assert utilities.is_before_midnight() is False
