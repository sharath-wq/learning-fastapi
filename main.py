from fastapi import FastAPI, HTTPException

app = FastAPI()

BOOKS = [
    {"id": 1, "title": "Title 1", "author": "Author 1", "category": "Science"},
    {"id": 2, "title": "Title 2", "author": "Author 2", "category": "Science"},
    {"id": 3, "title": "Title 3", "author": "Author 3", "category": "History"},
    {"id": 4, "title": "Title 4", "author": "Author 4", "category": "Math"},
    {"id": 5, "title": "Title 5", "author": "Author 5", "category": "Math"},
]


@app.get("/books/")
def read_all_books(category: str):
    print(category)
    if category:
        result = [b for b in BOOKS if b['category'].casefold() == category.casefold()]
        return result
    return BOOKS


@app.get("/books/{book_id}")
def read_one_book(book_id: int):
    book = next((b for b in BOOKS if b["id"] == book_id), None)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
