from app.database.BaseCrud import CRUDBase
from app.model.User import User


class UserDB(CRUDBase[User]):
    def __init__(self) -> None:
        super().__init__(model=User, collection_name="User")


user_db = UserDB()
