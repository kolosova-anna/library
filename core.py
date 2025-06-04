from dataclasses import dataclass

@dataclass
class Book():
    # свойсктва для описания книги
    title: str
    author: str
    genre: str
    book_count: int


