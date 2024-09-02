
from bson import ObjectId

from app.database.BallotDB import ballot_db
from app.model.Ballot import Ballot
from app.schema.Ballot import BallotInput


async def create_ballot(ballot : BallotInput, user_id : ObjectId) -> ObjectId:
    return await ballot_db.create(obj_in=Ballot(
        **ballot.model_dump(), user_id=user_id
    ))


async def read_ballot(object_id : ObjectId) -> Ballot | None:
    ballot = await ballot_db.get(filter_query={"_id": object_id})
    if not ballot:
        return None
    return ballot
