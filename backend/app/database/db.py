from sqlmodel import create_engine, Session
from dotenv import load_dotenv
import os

load_dotenv()

LOCAL_DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(LOCAL_DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
