from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field

from app.schema.Base import PyObjectId


class UserRole(str, Enum):
    PARTECIPANT = "partecipant"
    ADMIN = "admin"


class User(BaseModel):
    name : str
    email : str
    phone : str | None = Field(default=None)
    city : str | None = Field(default=None)

    role  : UserRole = UserRole.PARTECIPANT

    lottery_wins : list[PyObjectId] = Field(default=[])

    created: str = datetime.now().isoformat()
    updated: str = datetime.now().isoformat()
