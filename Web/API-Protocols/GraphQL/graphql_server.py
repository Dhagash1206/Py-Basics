# GraphQL: single endpoint, client chooses exactly the fields it needs.
# Run: uvicorn graphql_server:app --port 8002   (GraphiQL UI at /graphql)
import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Book:
    id: int
    title: str
    author: str


book_catalog: list[Book] = [
    Book(id=1, title="Dune", author="Frank Herbert"),
    Book(id=2, title="Neuromancer", author="William Gibson"),
]


@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> list[Book]:
        return book_catalog

    @strawberry.field
    def book(self, id: int) -> Book | None:
        return next((book for book in book_catalog if book.id == id), None)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        new_book = Book(id=len(book_catalog) + 1, title=title, author=author)
        book_catalog.append(new_book)
        return new_book


app = FastAPI()
app.include_router(GraphQLRouter(strawberry.Schema(query=Query, mutation=Mutation)), prefix="/graphql")
