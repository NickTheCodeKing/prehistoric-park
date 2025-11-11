from fastapi import APIRouter, status, HTTPException, Response, Depends
from ..database.crud import animal_crud
from ..database import db
from ..models import Animal
from ..models.enums import Sex, CautionLevel
from datetime import date, datetime


router = APIRouter()

@router.get("/animals", status_code=status.HTTP_200_OK)
def get_animals(
    *,
    session: db.Session = Depends(db.get_session),
    response: Response,
    id: str | None = None, 
    enclosureID: str | None = None, 
    animalName: str | None = None, 
    age: int | None = None, 
    sex: Sex | None = None, 
    species: str | None = None, 
    height: float | None = None, 
    length: float | None = None, 
    weight: float | None = None, 
    birthDate: date | None = None, 
    description: str | None = None,
    temperament: str | None = None,
    cautionLevel: CautionLevel | None = None,
    lastFeedDate: datetime | None = None,
    dnaSequence: str | None = None,
    deceased: bool | None = None,
    ):

    animals = animal_crud.select_animals(session=session, id=id, enclosureID=enclosureID, animalName=animalName, age=age, sex=sex, species=species, height=height, length=length, weight=weight, birthDate=birthDate, description=description, temperament=temperament, cautionLevel=cautionLevel, lastFeedDate=lastFeedDate, dnaSequence=dnaSequence, deceased=deceased)
    if not animals:
        response.status_code = status.HTTP_204_NO_CONTENT
    return animals

@router.get("/animals/{id}", status_code=status.HTTP_200_OK)
def get_animal(*, session: db.Session = Depends(db.get_session), id: str):

    animal = animal_crud.select_animal(session=session, id=id)

    if not animal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
    return animal

@router.post("/animals", status_code=status.HTTP_201_CREATED)
def post_animal(*, session: db.Session = Depends(db.get_session), animal: Animal):
    if animal.id == None:
        animal.id = animal_crud.generate_new_id(session)
    animal = animal_crud.create_animal(session=session, animal=animal)

    return animal

@router.patch("/animals/{id}", status_code=status.HTTP_200_OK)
def patch_animal(
    *,
    session: db.Session = Depends(db.get_session),
    id: str | None = None, 
    enclosureID: str | None = None, 
    animalName: str | None = None, 
    age: int | None = None, 
    sex: Sex | None = None, 
    species: str | None = None, 
    height: float | None = None, 
    length: float | None = None, 
    weight: float | None = None, 
    birthDate: date | None = None, 
    description: str | None = None,
    temperament: str | None = None,
    cautionLevel: CautionLevel | None = None,
    lastFeedDate: datetime | None = None,
    dnaSequence: str | None = None,
    deceased: bool | None = None
    ):
    animal = animal_crud.select_animal(id=id, session=session)

    if not animal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")

    return animal_crud.update_animal(session=session, animal=animal, enclosureID=enclosureID, animalName=animalName, age=age, sex=sex, species=species, height=height, length=length, weight=weight, birthDate=birthDate, description=description, temperament=temperament, cautionLevel=cautionLevel, lastFeedDate=lastFeedDate, dnaSequence=dnaSequence, deceased=deceased)

@router.put("/animals/{id}", status_code=status.HTTP_200_OK)
def put_animal(*, session: db.Session = Depends(db.get_session), id: str, new_animal: Animal):
    old_animal = animal_crud.select_animal(id=id, session=session)

    if not old_animal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")

    animal = animal_crud.replace_animal(session=session, new_animal=new_animal, old_animal=old_animal)

    return animal

@router.delete("/animals/{id}", status_code=status.HTTP_200_OK)
def delete_animal(*, session: db.Session = Depends(db.get_session), id: str):
    animal = animal_crud.select_animal(session=session, id=id)

    if not animal:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Animal not found")
    else:
        animal = animal_crud.remove_animal(session=session, animal=animal)

    return animal

