from core_interfaces import Book, Author, Genre, BookInfo, IBooksRepo, IAuthorsRepo, IGenresRepo


class UnitOfWork:
    ''' Реализация методов для работы с книгами '''
    def __init__(self, books_lib: IBooksRepo, authors_lib: IAuthorsRepo, genres_lib: IGenresRepo):
        self.books_lib = books_lib
        self.authors_lib = authors_lib
        self.genres_lib = genres_lib
#        self.book_service = BookService(self)
#        self.author_service = AuthorsService(self)
#        self.genre_service = GenresService(self)
#        self.recomendations = Recomendations(self)


class BookService:
    ''' методы для работы с книгами '''
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def get_books(self) -> list[BookInfo]:
        return self.uow.books_lib.get_books()

    def add_book(self, title: str, author_id: int, genre_id: int) -> None:
        return self.uow.books_lib.add_book(title, author_id, genre_id)
    
    def get_last_book(self) -> BookInfo:
        return self.uow.books_lib.get_last_book()

    def mark_as_read(self, book_id: int) -> None:
        return self.uow.books_lib.mark_as_read(book_id)
    
    def get_book_by_id(self, book_id: int) -> Book:
        return self.uow.books_lib.get_book_by_id(book_id)
    
    def find_books(self, **filters) -> list:
        # поиск книг по названию ,автору или жанру
        return self.uow.books_lib.find_books(**filters)
    
    def check_book_id(self, book_id: int) -> bool:
        # проверка наличия книги в базе по переданному id
        return self.uow.books_lib.check_book_id(book_id)
    

class AuthorsService:
    ''' Методы для работы с авторами '''

    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def add_author(self, name_author: str) -> None:
        return self.uow.authors_lib.add_author(name_author)
    
    def get_last_author(self) -> Author:
        return self.uow.authors_lib.get_last_author()
    
    def get_authors(self) -> list[Author]:
        return self.uow.authors_lib.get_authors()
    
    def check_author_id(self, author_id: int) -> bool:
        # проверка наличия автора в базе по переданному id
        return self.uow.authors_lib.check_author_id(author_id)
    
    def check_name_author(self, name_author: str) -> bool:
        # проверка наличия автора по имени
        return self.uow.authors_lib.check_name_author(name_author)


class GenresService:
    ''' Методы для работы с жанрами '''
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def add_genre(self, name_genre: str) -> None:
        return self.uow.genres_lib.add_genre(name_genre)
    
    def get_last_genre(self) -> Genre:
        return self.uow.genres_lib.get_last_genre()
    
    def get_genres(self) -> list[Genre]:
        return self.uow.genres_lib.get_genres()
    
    def check_genre_id(self, genre_id: int) -> bool:
        # проверка наличия жанра в базе по переданному id
        return self.uow.genres_lib.check_genre_id(genre_id)
    
    def check_name_genre(self, name_genre: str) -> bool:
        # проверка наличия жанра по названию
        return self.uow.genres_lib.check_name_genre(name_genre)


class Recomendations:    
    ''' Формирует список рекомендаций '''
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def get_recomendations(self) -> list[BookInfo]:
        books_list = self.uow.books_lib.get_books()
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