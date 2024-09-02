
from pydantic import field_validator

from app.schema.Base import Base


class BallotInput(Base):
    numbers : list[int]

    @field_validator('numbers', mode='before')
    def check_numbers(cls, v):
        if len(v) != 6 or not all(isinstance(i, int) for i in v):
            raise ValueError('Numbers need to be less than 6.')
        return v
