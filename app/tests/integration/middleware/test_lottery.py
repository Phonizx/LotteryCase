from unittest.mock import patch

import pytest
from bson import ObjectId

from app.database.BallotDB import ballot_db
from app.database.LotteryDB import lottery_db
from app.database.WinnerDB import winner_db
from app.middleware.Lottery import close_lottery
from app.model.Ballot import Ballot
from app.model.Lottery import Lottery
from app.model.Winner import Winner


@pytest.mark.asyncio
async def test_insert_document():
    user_id = ObjectId()
    magic_numbers = [1,2,3,4,5,6]
    mock_ballot = Ballot(
        numbers=magic_numbers, user_id=user_id
    )
    ballot_mock_id = await ballot_db.create(
        mock_ballot
    )

    with patch("app.middleware.Lottery.generate_lottery_numbers", return_value=magic_numbers):
        close_lottery()

    winner : Winner = await  winner_db.get({"ballot_id": ObjectId(ballot_mock_id)})
    lottery_id = winner.lottery_id
    lottery : Lottery = await lottery_db.get({"_id": ObjectId(lottery_id)})

    assert winner.user_id == user_id
    assert lottery.numbers == magic_numbers
    assert winner.prize == 6
