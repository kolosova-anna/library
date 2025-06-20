from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Book:
    book_id: int
    title: str
    author_id: int
    genre_id: int
    is_read: bool = False


@dataclass
class Author:
    author_id: int
    name_author: str


@dataclass
class Genre:
    genre_id: int
    name_genre: str


@dataclass
class BookInfo:
    ''' Полная информация о книге, объединенные данные '''
    book_id: int
    title: str
    author_id: int
    name_author: str
    genre_id: int
    name_genre: str
    is_read: bool


class BooksLib(ABC):
    ''' Интерфейс для работы с книгами '''
    
    @abstractmethod
    def get_books(self) -> list[BookInfo]:
        pass

    @abstractmethod
    def add_book(self, title: str, author_id: int, genre_id: int) -> None:
        pass

    @abstractmethod
    def get_last_book(self) -> BookInfo:
        pass

    @abstractmethod
    def mark_as_read(self, book_id: int) -> None:
        pass
    
    @abstractmethod
    def get_book_by_id(self, book_id: int) -> Book:
        pass

    @abstractmethod
    def find_books(self, **filters: dict) -> list[BookInfo]:
        pass

    @abstractmethod
    def check_book_id(self, book_id: int) -> bool:
        pass
    

class AuthorsLib(ABC):
    ''' Интерфейс для работы с авторами '''

    @abstractmethod
    def add_author(self, name_author: str) -> None:
        pass

    @abstractmethod
    def get_last_author(self) -> Author:
        pass

    @abstractmethod
    def get_authors(self) -> list[Author]:
        pass

    @abstractmethod
    def check_author_id(self, author_id: int) -> bool:
        pass

    @abstractmethod
    def check_name_author(self, name_author: str) -> bool:
        pass


class GenresLib(ABC):
    ''' Интерфейс для работы с жанрами '''

    @abstractmethod
    def add_genre(self, name_genre: str) -> None:
        pass

    @abstractmethod
    def get_last_genre(self) -> Genre:
        pass

    @abstractmethod
    def get_genres(self) -> list[Genre]:
        pass

    @abstractmethod
    def check_genre_id(self, genre_id: int) -> bool:
        pass

    @abstractmethod
    def check_name_genre(self, name_genre: str) -> bool:
        pass
    
    


