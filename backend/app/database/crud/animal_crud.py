from .. import db
from sqlmodel import select, func
from ...models import Animal
from ...models.enums import Sex, CautionLevel
from datetime import datetime, date

def select_animals(
    session: db.Session | None = None,
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
    if session is None:
        session = db.get_session()
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

def select_animal(*, session: db.Session | None = None, id: str):
    if not session:
        session = db.get_session()
    return session.exec(select(Animal).where(Animal.id == id)).first()

def create_animal(*, session: db.Session | None = None, animal: Animal):
    if not session:
        session = db.get_session()

    session.add(animal)
    session.commit()
    animal = session.exec(select(Animal).where(Animal.id == animal.id)).first()

    return animal

def update_animal(
    *,
    session: db.Session | None = None,
    animal: Animal,
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
    if not session:
        session = db.get_session()
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

def replace_animal(*, session: db.Session | None = None, new_animal: Animal, old_animal: Animal):
    if not session:
        session = db.get_session()
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

def remove_animal(*, session: db.Session | None = None, animal: Animal):
    if not session:
        session = db.get_session()
    session.delete(animal)
    session.commit()

    return session.exec(select(Animal).where(Animal.id == animal.id)).first()

def generate_new_id(session: db.Session | None = None):
    if not session:
        session = db.get_session()
    result = session.exec(func.max(Animal.id)).first()
    max_id_str = result[0]
    max_id_int = int(max_id_str)
    id_int = max_id_int + 1
    id_int_str = str(id_int)
    id_int_str = id_int_str.zfill(10)
    return id_int_str