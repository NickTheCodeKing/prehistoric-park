from fastapi import FastAPI, status

from typing import Union
from pydantic import BaseModel
from dotenv import load_dotenv
from sqlmodel import create_engine, Field, Session, SQLModel, select
from datetime import datetime, date
from enum import Enum
import os

# Load database credentials
load_dotenv()

LOCAL_DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(LOCAL_DATABASE_URL, echo=True)

app = FastAPI()

class Sex(str, Enum):
    male = "male"
    female = "female"
    herm = "herm"
    other = "other"

class CautionLevel(str, Enum):
    none = "none"
    low = "low"
    medium = "medium"
    high = "high"

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

@app.get("/animals", status_code=status.HTTP_200_OK)
def get_animals(
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
    return select_animals(id, enclosureID, animalName, age, sex, species, height, length, weight, birthDate, description, temperament, cautionLevel, lastFeedDate, dnaSequence, deceased)
        
    
@app.get("/animals/{id}", status_code=status.HTTP_200_OK)
def get_animal(id: str):
    return select_animal(id)

@app.post("/animals", status_code=status.HTTP_201_CREATED)
def post_animal(animal: Animal):
    animal = create_animal(animal)

    return animal
    

@app.patch("/animals/{id}", status_code=status.HTTP_200_OK)
def patch_animal(id: str | None = None, 
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
    animal = select_animal(id)
    return update_animal(animal, enclosureID, animalName, age, sex, species, height, length, weight, birthDate, description, temperament, cautionLevel, lastFeedDate, dnaSequence, deceased)  
        
@app.put("/animals/{id}", status_code=status.HTTP_200_OK)
def put_animal(id: str, new_animal: Animal):
    old_animal = select_animal(id)

    animal = replace_animal(new_animal, old_animal)

    return animal
    

def select_animals(
    id: str | None = None, 
    enclosureID: str | None = None, 
    animalName: str | None = None, 
    age: int | None = None, 
    sex: str | None = None, 
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
    with Session(engine) as session:
        statement = select(Animal)
        if id:
            statement = statement.where(Animal.id == id)
        if enclosureID:
            statement = statement.where(Animal.enclosureID == enclosureID)
        if animalName:
            statement = statement.where(Animal.animalName == animalName)
        if age:
            statement = statement.where(Animal.age == age)
        if sex:
            statement = statement.where(Animal.sex == sex)
        if species:
            statement = statement.where(Animal.species == species)
        if height:
            statement = statement.where(Animal.height == height)
        if length:
            statement = statement.where(Animal.length == length)
        if weight:
            statement = statement.where(Animal.weight == weight)
        if birthDate:
            statement = statement.where(Animal.birthDate == birthDate)
        if description:
            statement = statement.where(Animal.description == description)
        if temperament:
            statement = statement.where(Animal.temperament == temperament)
        if cautionLevel:
            statement = statement.where(Animal.cautionLevel == cautionLevel)
        if lastFeedDate:
            statement = statement.where(Animal.lastFeedDate == lastFeedDate)
        if dnaSequence:
            statement = statement.where(Animal.dnaSequence == dnaSequence)
        if deceased:
            statement = statement.where(Animal.deceased == deceased)

            
        return session.exec(statement).all()
    
def select_animal(id: str):
    with Session(engine) as session:
        return session.exec(select(Animal).where(Animal.id == id)).one()
    
def create_animal(animal: Animal):
    with Session(engine) as session:
        session.add(animal)
        session.commit()

        return animal
    
def update_animal(animal: Animal,
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
    with Session(engine) as session:
        if enclosureID:
            animal.enclosureID = enclosureID
        if animalName:
            animal.animalName = animalName
        if age:
            animal.age = age
        if sex:
            animal.sex = sex
        if species:
            animal.species = species
        if height:
            animal.height = height
        if length:
            animal.length = length
        if weight:
            animal.weight = weight
        if birthDate:
            animal.birthDate = birthDate
        if description:
            animal.description = description
        if temperament:
            animal.temperament = temperament
        if cautionLevel:
            animal.cautionLevel = cautionLevel
        if lastFeedDate:
            animal.lastFeedDate = lastFeedDate
        if dnaSequence:
            animal.dnaSequence = dnaSequence
        if deceased:
            animal.deceased = deceased
        
        session.add(animal)
        session.commit()
        session.refresh(animal)

        return animal
    
def replace_animal(new_animal: Animal, old_animal: Animal):
    with Session(engine) as session:
        old_animal.enclosureID = new_animal.enclosureID
        old_animal.animalName = new_animal.animalName
        old_animal.age = new_animal.age
        old_animal.sex = new_animal.sex
        old_animal.species = new_animal.species
        old_animal.height = new_animal.height
        old_animal.length = new_animal.length
        old_animal.weight = new_animal.weight
        old_animal.birthDate = new_animal.birthDate
        old_animal.description = new_animal.description
        old_animal.temperament = new_animal.temperament
        old_animal.cautionLevel = new_animal.cautionLevel
        old_animal.lastFeedDate = new_animal.lastFeedDate
        old_animal.dnaSequence = new_animal.dnaSequence
        old_animal.deceased = new_animal.deceased

        session.add(old_animal)
        session.commit()
        session.refresh(old_animal)

        return old_animal

    

    
def main():
    animal = Animal(id="0000000011",enclosureID="000022",animalName="Test",age=6,sex="Male",species="Utahraptor ostrommaysi",birthDate="2018-09-03",description="Utahraptor was a meat-eating dinosaur that lived in what's now North America. It was a member of the dromaeosaur group, like Velociraptor. But Utahraptor was much larger, the largest known member of this group.It was much stockier than many of its relatives. Some other dromaeosaurs were very small and slim.",cautionLevel="low",deceased=False)

    animal = create_animal(animal)

    return
   

if __name__ == "__main__":
    main()
