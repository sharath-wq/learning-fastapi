from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {
        "id": 1,
        "title": "Book1",
        "price": 200,
    }
]


@app.get("/")
def first_api():
    return BOOKS
