from typing import Annotated

from bson import ObjectId
from fastapi import APIRouter, Header, Response, status

import app.utils as utilities
from app.middleware.Ballot import create_ballot, read_ballot
from app.middleware.Partecipant import read_partecipant
from app.model.Ballot import Ballot
from app.schema.Ballot import BallotInput
from app.schema.Base import PyObjectIdOutput
from app.schema.User import PartecipantOuput

ballot_router = APIRouter(
    prefix="/ballots",
    tags=["Ballots"],
    responses={404: {"description": "Not Found"}},
)


@ballot_router.post("", response_model=PyObjectIdOutput)
async def issuing_ballot_api(ballot : BallotInput, lottery_x_token: Annotated[str | None, Header()] = None) -> PyObjectIdOutput | Response:
    if not lottery_x_token:
        return Response(content="Partecipant needs to be registered.", status_code=status.HTTP_401_UNAUTHORIZED)

    if not utilities.is_before_midnight():
        return Response(content="Partecipant can issue ballots before midninght.", status_code=status.HTTP_400_BAD_REQUEST)

    partecipant: PartecipantOuput | None = await read_partecipant(object_id=ObjectId(lottery_x_token))
    if not partecipant:
        return Response(content="yolo", status_code=status.HTTP_400_BAD_REQUEST)

    inserted_ballot_id = await create_ballot(ballot=ballot, user_id=lottery_x_token)
    return PyObjectIdOutput(inserted_id=inserted_ballot_id)


@ballot_router.get("/{id}", response_model=Ballot)
async def get_ballot_api(id: str) -> Ballot | Response:
    ballot : Ballot | None = await read_ballot(object_id=ObjectId(id))
    if not ballot:
        return Response(content="Ballot not found.", status_code=status.HTTP_404_NOT_FOUND)
    return ballot
