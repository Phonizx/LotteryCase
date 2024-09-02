from app.database.BaseCrud import CRUDBase
from app.model.Winner import Winner


class WinnerDB(CRUDBase[Winner]):
    def __init__(self) -> None:
        super().__init__(model=Winner, collection_name="Winner")


winner_db = WinnerDB()
