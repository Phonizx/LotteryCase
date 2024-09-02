from bson import ObjectId

from app.database.UserDB import user_db
from app.model.User import User
from app.schema.User import CreatePartecipant, EditPartecipant, PartecipantOuput


async def create_partecipant(partecipant : CreatePartecipant) -> ObjectId:
    user = User(**partecipant.model_dump())
    return await user_db.create(obj_in=user)


async def read_partecipant(object_id : ObjectId) -> PartecipantOuput | None:
    user = await user_db.get(filter_query={"_id": object_id})
    if not user:
        return None
    return PartecipantOuput(**user.model_dump())


async def update_partecipant(object_id : ObjectId, partecipant_update : EditPartecipant) -> PartecipantOuput:
    user = await read_partecipant(object_id=object_id)
    user.__dict__.update(
        partecipant_update.model_dump(exclude_none=True)
    )
    return await user_db.update(filter_query={"_id": object_id}, updated_obj=user)


async def delete_partecipant(object_id : ObjectId):
    return await user_db.delete(filter_query={"_id": object_id})
