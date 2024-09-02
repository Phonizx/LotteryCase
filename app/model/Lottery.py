from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class LotteryPrizeType(int, Enum):
    PAIR = 2
    TRIPLET = 3
    QUADRUPLET = 4
    QUINTUPLET = 5
    JACKPOT = 6

class Lottery(BaseModel):
    numbers : list[int]
    lottery_date : datetime = datetime.now()

    has_any_winner : bool = False
    lottery_prizes : list[LotteryPrizeType] = []
    winner_city : str | None = None
