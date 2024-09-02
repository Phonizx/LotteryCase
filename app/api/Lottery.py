from datetime import date

from fastapi import APIRouter, Query, Response, status

from app.middleware.Lottery import find_lottery_by_datetime
from app.model.Lottery import Lottery

lottery_router = APIRouter(
    prefix="/lottery",
    tags=["lottery"],
    responses={404: {"description": "Not Found"}},
)


@lottery_router.get("/find", response_model=Lottery)
async def find_lottery_api(date_input: date = Query()) -> Lottery | Response:
    lottery = await find_lottery_by_datetime(date_input=date_input)
    if not lottery:
        return Response(content="Lottery not found.", status_code=status.HTTP_404_NOT_FOUND)
    return lottery
