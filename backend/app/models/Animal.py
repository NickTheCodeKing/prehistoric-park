from sqlmodel import SQLModel, Field
from datetime import datetime, date
from .enums import Sex, CautionLevel

class Animal(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    enclosureID: str
    animalName: str
    age: int | None = None
    sex: Sex
    species: str
    height: float | None = None
    length: float | None = None
    weight: float | None = None
    birthDate: date
    description: str | None = None
    temperament: str | None = None
    cautionLevel: CautionLevel
    lastFeedDate: datetime | None = None
    dnaSequence: str | None = None
    deceased: bool | None = None