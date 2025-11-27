from sqlmodel import create_engine, Session, SQLModel
from dotenv import load_dotenv
import os

load_dotenv()

USE_TEST_DB = os.getenv("USE_TEST_DB", "false").lower() == "true"

DATABASE_URL = (
    os.environ["TEST_DATABASE_URL"]
    if USE_TEST_DB
    else os.environ["DATABASE_URL"]
)

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
