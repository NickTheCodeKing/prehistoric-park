from .routers import animals
from fastapi import FastAPI


app = FastAPI()

app.include_router(animals.router)

@app.get("/")
def root():
    return {"message": "Hello World!"}

def main():
    return

if __name__ == "__main__":
    main()
