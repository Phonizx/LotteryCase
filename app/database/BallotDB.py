from app.database.BaseCrud import CRUDBase
from app.model.Ballot import Ballot


class BallotDB(CRUDBase[Ballot]):
    def __init__(self) -> None:
        super().__init__(model=Ballot, collection_name="Ballot")


ballot_db = BallotDB()
