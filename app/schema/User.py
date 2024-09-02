from app.model.User import Field, User
from app.schema.Base import Base


class CreatePartecipant(Base):
    name : str
    email : str
    phone : str | None = Field(default=None)
    city : str | None = Field(default=None)


class PartecipantOuput(User):
    pass


class EditPartecipant(Base):
    name : str | None = Field(default=None)
    email : str | None = Field(default=None)
    phone : str | None = Field(default=None)
    city : str | None = Field(default=None)
