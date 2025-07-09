from core_interfaces import Book, Author, Genre, BookInfo, IBooksRepo, IAuthorsRepo, IGenresRepo


class UnitOfWork:
    ''' Реализация методов для работы с книгами '''
    def __init__(self, books_repo: IBooksRepo, authors_repo: IAuthorsRepo, genres_repo: IGenresRepo):
        self.books_repo = books_repo
        self.authors_repo = authors_repo
        self.genres_repo = genres_repo


class BookService:
    ''' методы для работы с книгами '''
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def get_books(self) -> list[BookInfo]:
        return self.uow.books_repo.get_books()

    def add_book(self, title: str, author_id: int, genre_id: int) -> int | None:
        return self.uow.books_repo.add_book(title, author_id, genre_id)
    
    def mark_as_read(self, book_id: int) -> None:
        return self.uow.books_repo.mark_as_read(book_id)
    
    def get_book_by_id(self, book_id: int) -> BookInfo:
        return self.uow.books_repo.get_book_by_id(book_id)
    
    def find_books(self, param: str, value: str) -> list[BookInfo]:
        # поиск книг по названию ,автору или жанру
        if param:
            return self.uow.books_repo.find_books(param, value)
        else:
            raise ValueError("Missing argument for the function")
    
    def check_book_id(self, book_id: int) -> bool:
        # проверка наличия книги в базе по переданному id
        return self.uow.books_repo.check_book_id(book_id)
  

class AuthorsService:
    ''' Методы для работы с авторами '''

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def add_author(self, name_author: str) -> int | None:
        return self.uow.authors_repo.add_author(name_author)
    
    def get_author_by_id(self, author_id: int) -> Author:
        return self.uow.authors_repo.get_author_by_id(author_id)
    
    def get_authors(self) -> list[Author]:
        return self.uow.authors_repo.get_authors()
    
    def check_author_id(self, author_id: int) -> bool:
        # проверка наличия автора в базе по переданному id
        return self.uow.authors_repo.check_author_id(author_id)
    

class GenresService:
    ''' Методы для работы с жанрами '''
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def add_genre(self, name_genre: str) -> int | None:
        return self.uow.genres_repo.add_genre(name_genre)
    
    def get_genre_by_id(self, genre_id: int) -> Genre:
        return self.uow.genres_repo.get_genre_by_id(genre_id)
    
    def get_genres(self) -> list[Genre]:
        return self.uow.genres_repo.get_genres()
    
    def check_genre_id(self, genre_id: int) -> bool:
        # проверка наличия жанра в базе по переданному id
        return self.uow.genres_repo.check_genre_id(genre_id)
    

class Recomendations:    
    ''' Формирует список рекомендаций '''
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def get_recomendations(self) -> list[BookInfo]:
        books_list = self.uow.books_repo.get_books()
        read_books = [b for b in books_list if b.is_read]
        unread_books = [b for b in books_list if not b.is_read]
        read_genres = [b.genre_id for b in read_books]

        recomendations = []
        for b in unread_books:
            if b.genre_id in read_genres:
                recomendations.append(b)
        
        if not recomendations:
            read_authors = [b.author_id for b in read_books]
            for b in unread_books:
                if b.author_id in read_authors:
                    recomendations.append(b)
        
        if not recomendations:
            recomendations = unread_books
        
        return recomendations[:10]
    

class Exceptions(Exception):

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return f'Ошибка: {self.message}'