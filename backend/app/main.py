from fastapi import FastAPI

from typing import Union
from pydantic import BaseModel
from dotenv import load_dotenv
from sqlmodel import create_engine, Field, Session, SQLModel, select
from datetime import datetime
import os

# Load database credentials
load_dotenv()

LOCAL_DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(LOCAL_DATABASE_URL, echo=True)

app = FastAPI()

class Animal(SQLModel, table=True):
    id: str | None = Field(default=None, primary_key=True)
    enclosureID: str | None = None
    animalName: str | None = None
    age: int | None = None
    sex: str | None = None
    species: str | None = None
    height: float | None = None
    length: float | None = None
    weight: float | None = None
    birthDate: datetime | None = None
    description: str | None = None
    temperament: str | None = None
    cautionLevel: str | None = None
    lastFeedDate: datetime | None = None
    dnaSequence: str | None = None
    deceased: bool | None = None

@app.get("/animals")
def get_animals(
    id: str | None = None, 
    enclosureID: str | None = None, 
    animalName: str | None = None, 
    age: int | None = None, 
    sex: str | None = None, 
    species: str | None = None, 
    height: float | None = None, 
    length: float | None = None, 
    weight: float | None = None, 
    birthDate: datetime | None = None, 
    description: str | None = None,
    temperament: str | None = None,
    cautionLevel: str | None = None,
    lastFeedDate: datetime | None = None,
    dnaSequence: str | None = None,
    deceased: bool | None = None
    ):
    return select_animals(id, enclosureID, animalName, age, sex, species, height, length, weight, birthDate, description, temperament, cautionLevel, lastFeedDate, dnaSequence, deceased)
        
    
@app.get("/animals/{id}")
def get_animal(id: str):
    return select_animal(id)
        
    
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
    birthDate: datetime | None = None, 
    description: str | None = None,
    temperament: str | None = None,
    cautionLevel: str | None = None,
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
    
def select_animal(id):
    with Session(engine) as session:
        return session.exec(select(Animal).where(Animal.id == id)).one()
    

    
def main():
    animals = select_animals()

    print(animals)

    return
   

if __name__ == "__main__":
    main()
