from .routers import animals
from fastapi import FastAPI
from .database.db import init_db


app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(animals.router)

@app.get("/")
def root():
    return {"message": "Hello World!"}

def main():
    return

if __name__ == "__main__":
    main()
