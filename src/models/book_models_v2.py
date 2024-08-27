from pydantic import BaseModel


class Author(BaseModel):
    id: str
    name: str
    birthdate: str
    nationality: str


class Book(BaseModel):
    id: str
    name: str
    author: Author
    publication_year: int
    genre: str