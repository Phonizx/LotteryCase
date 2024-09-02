import random
from datetime import date, datetime, timedelta, timezone

from app.database.BallotDB import ballot_db
from app.database.LotteryDB import lottery_db
from app.database.WinnerDB import winner_db
from app.model.Lottery import Lottery, LotteryPrizeType
from app.model.Winner import Winner


async def find_lottery_by_datetime(date_input : date) -> Lottery | None:
    start_of_day = datetime.combine(date_input, datetime.min.time(), tzinfo=timezone.utc)
    end_of_day = datetime.combine(date_input, datetime.max.time(), tzinfo=timezone.utc)
    return await lottery_db.get(
        filter_query={
            "lottery_date": {"$gte": start_of_day, "$lt": end_of_day}
        }
    )


def fetch_winners(lottery_numbers):
    project = {
        '$project': {
            'numbers': 1,
            'matches': {
                '$size': {
                    '$setIntersection': [
                        '$numbers', lottery_numbers
                    ]
                }
            },
            "user_id": 1,
            "issued": 1
    }}
    start_of_day = datetime.combine(datetime.now(), datetime.min.time(), tzinfo=timezone.utc)
    end_of_day = start_of_day + timedelta(days=1)
    match = {

        '$match': {
            "issued": {
                "$gte": start_of_day,
                "$lt": end_of_day
            },
            'matches': {
                '$gte': 2
        }}}

    group = {
        '$group': {
            '_id': '$matches',
            'winners': {
                '$push': '$$ROOT'
        }}}

    pipeline = [
        project,
        match,
        group,
    ]
    cursor =  ballot_db.pipeline_sync(collection="Ballot", pipeline=pipeline)

    winner_ballots = []
    for document in cursor:
        winner_ballots.append(document)
    return winner_ballots


def generate_lottery_numbers():
    return random.sample(range(1, 91), 6)

def close_lottery():
    lottery_numbers = generate_lottery_numbers()
    lottery = Lottery(
        numbers=lottery_numbers,
    )
    inserted_lottery_id = lottery_db.create_sync(obj_in=lottery, collection="Lottery")
    # log here inserted id
    # check possibile winners
    winner_ballots = fetch_winners(lottery_numbers=lottery_numbers)


    if not winner_ballots:
        return

    for winner in winner_ballots[0]["winners"]:
        winner_db.create_sync(obj_in=Winner(
            lottery_id=inserted_lottery_id,
            ballot_id=winner["_id"],
            prize=LotteryPrizeType(winner["matches"]),
            user_id=winner["user_id"],
            lottery_date=lottery.lottery_date
        ),collection="Winner")
        # emit win notification to the user
