from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Book():
    # свойсктва для описания книги
    book_id: int
    title: str
    author_id: int
    genre_id: int
    is_availiable: bool = True

@dataclass
class Author():
    # свойсктва для описания автора
    author_id: int
    name_author: str

@dataclass
class Genre():
    # свойсктва для описания жанра
    genre_id: int
    name_genre: str

class Books(ABC):
    # интерфейс для работы с книгами
    
    @abstractmethod
    def get_books(self) -> dict[int, Book]:
        pass

    @abstractmethod
    def add_book(self, book: Book) -> Book:
        pass

    @abstractmethod
    def change_is_availiable(self, book_id: int) -> None:
        pass


class Authors(ABC):
    # интерфейс для работы с авторами

    @abstractmethod
    def get_authors(self) -> dict[int, Author]:
        pass

    @abstractmethod
    def add_author(self, name_author: str) -> Author:
        pass


class Genres(ABC):
    # интерфейс для работы с жанрами

    @abstractmethod
    def get_genres(self) -> dict[int, Genre]:
        pass
    
    @abstractmethod
    def add_genre(self, name_genre: str) -> Genre:
        pass



