from datetime import datetime

from pydantic import BaseModel

from app.model.Lottery import LotteryPrizeType
from app.schema.Base import PyObjectId


class Winner(BaseModel):
    lottery_id : PyObjectId
    ballot_id : PyObjectId
    lottery_date : datetime
    prize : LotteryPrizeType
    user_id : PyObjectId
