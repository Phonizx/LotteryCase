import motor
import pytest
from pymongo.errors import ConnectionFailure

from app.settings import settings


@pytest.fixture(scope="session")
async def fix_db_connection():
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_CONNECTION_STRING)
    db = client['Lottery']

    try:
        await client.admin.command('ping')  # Verify connection
    except ConnectionFailure:
        pytest.fail("MongoDB connection failed")

    yield db
    client.drop_database('Lottery')
    client.close()
