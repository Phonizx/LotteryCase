from datetime import datetime

from pydantic import BaseModel

from app.schema.Base import PyObjectId


class Ballot(BaseModel):
    numbers : list[int]
    user_id : PyObjectId
    issued: datetime = datetime.now()
