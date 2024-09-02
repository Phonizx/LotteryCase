
from bson import ObjectId
from fastapi import APIRouter, Response, status

from app.middleware.Partecipant import (
    create_partecipant,
    delete_partecipant,
    read_partecipant,
    update_partecipant,
)
from app.schema.Base import PyObjectIdOutput
from app.schema.User import CreatePartecipant, EditPartecipant, PartecipantOuput

partecipant_router = APIRouter(
    prefix="/partecipants",
    tags=["Partecipant"],
    responses={404: {"description": "Not Found"}},
)


@partecipant_router.post("", response_model=PyObjectIdOutput)
async def create_partecipant_api(partecipant : CreatePartecipant) -> PyObjectIdOutput:
    inserted_user_id = await create_partecipant(partecipant=partecipant)
    return PyObjectIdOutput(inserted_id=inserted_user_id)


@partecipant_router.get("/{id}", response_model=PartecipantOuput)
async def get_partecipant_api(id: str) -> PartecipantOuput | Response:
    partecipant: PartecipantOuput | None = await read_partecipant(object_id=ObjectId(id))
    if not partecipant:
        return Response(content="Partecipant not found.", status_code=status.HTTP_404_NOT_FOUND)
    return partecipant


@partecipant_router.patch("/{id}", response_model=PartecipantOuput)
async def edit_partecipant_api(id : str, updated_pilot : EditPartecipant) -> PartecipantOuput | Response:
    pilot : PartecipantOuput = await update_partecipant(object_id=ObjectId(id), partecipant_update=updated_pilot)
    if not pilot:
        return Response(content="Partecipant not found.", status_code=status.HTTP_404_NOT_FOUND)
    return pilot


@partecipant_router.delete("/{id}")
async def delete_pilot_view(id : str) -> Response:
    await delete_partecipant(object_id=ObjectId(id))
    return Response(status_code=status.HTTP_204_NO_CONTENT)
