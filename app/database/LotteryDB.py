from app.database.BaseCrud import CRUDBase
from app.model.Lottery import Lottery


class LotteryDB(CRUDBase[Lottery]):
    def __init__(self) -> None:
        super().__init__(model=Lottery, collection_name="Lottery")


lottery_db = LotteryDB()
