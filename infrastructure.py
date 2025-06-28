import sqlite3
from core_interfaces import Book, Author, Genre, BookInfo, IBooksRepo, IAuthorsRepo, IGenresRepo


class DBConnectMethods:
    ''' Содержит метода для подключения к БД и передачи запроса '''

    def __init__(self, db: str):
        self.db = db
        self.connection = sqlite3.connect(self.db)

    def execute_query(self, query: str, *args) -> None:
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(query, args)

    def execute_get_data(self, query: str, *args) -> list:
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(query, args)
            result: list = cursor.fetchall()
        return result
    
    def get_int(self, query: str, *args) -> int:
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute(query, args)
            result: tuple = cursor.fetchone()
        return result[0]
    
    def close(self) -> None:
        self.connection.close()


class AuthorsRepo(IAuthorsRepo):
    ''' Содержит методы для хранения и обработки данных об авторах '''

    def __init__(self, db):
        self.db: DBConnectMethods = db
        query = '''
            CREATE TABLE IF NOT EXISTS authors (
                    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_author TEXT UNIQUE
                    )
        '''
        self.db.execute_query(query)

    def add_author(self, name_author: str) -> None:
        query = "INSERT INTO authors (name_author) VALUES (?)"
        self.db.execute_query(query, name_author)
    
    def get_last_author(self) -> Author:
        query = '''
            SELECT author_id, name_author
            FROM authors
            ORDER BY author_id DESC
            LIMIT 1
        '''
        authors = self.db.execute_get_data(query)
        authors_list = [Author(*row) for row in authors]
        return authors_list[0]

    def get_authors(self) -> list[Author]:
        query = "SELECT author_id, name_author FROM authors"
        authors = self.db.execute_get_data(query)
        authors_list = [Author(*row) for row in authors]
        return authors_list
    
    def check_author_id(self, author_id: int) -> bool:
        # проверка наличия автора в базе по переданному id
        query = "SELECT COUNT(*) FROM authors WHERE author_id = ?"
        res = self.db.get_int(query, author_id)
        if res == 1:
            return True
        return False
    
    def check_name_author(self, name_author: str) -> bool:
        # проверка наличия автора в базе по имени
        query = "SELECT COUNT(*) FROM authors WHERE name_author = ?"
        res = self.db.get_int(query, name_author)
        if res == 1:
            return True
        return False


class GenresRepo(IGenresRepo):
    ''' Содержит методы для хранения и обработки данных о жанрах '''

    def __init__(self, db):
        self.db: DBConnectMethods = db
        query = '''
            CREATE TABLE IF NOT EXISTS genres (
                    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_genre TEXT UNIQUE
                    )
        '''
        self.db.execute_query(query)

    def add_genre(self, name_genre: str) -> None:
        query = "INSERT INTO genres (name_genre) VALUES (?)"
        self.db.execute_query(query, name_genre)

    def get_last_genre(self) -> Genre:
        query = '''
            SELECT genre_id, name_genre
            FROM genres
            ORDER BY genre_id DESC
            LIMIT 1
        '''
        genres = self.db.execute_get_data(query)
        genres_list = [Genre(*row) for row in genres]
        return genres_list[0]

    def get_genres(self) -> list[Genre]:
        query = "SELECT genre_id, name_genre FROM genres"
        genres = self.db.execute_get_data(query)
        genres_list = [Genre(*row) for row in genres]
        return genres_list
    
    def check_genre_id(self, genre_id: int) -> bool:
        # проверка наличия жанра в базе по переданному id
        query = "SELECT COUNT(*) FROM genres WHERE genre_id = ?"
        res = self.db.get_int(query, genre_id)
        if res == 1:
            return True
        return False
    
    def check_name_genre(self, name_genre: str) -> bool:
        # проверка наличия жанра в базе по названию
        query = "SELECT COUNT(*) FROM genres WHERE name_genre = ?"
        res = self.db.get_int(query, name_genre)
        if res == 1:
            return True
        return False

class BooksRepo(IBooksRepo):
    ''' Cодержит методы для хранения и обработки данных о книгах '''
   
    def __init__(self, db):
    # иниуциализация БД и создание таблицы с книгами
        self.db: DBConnectMethods = db
        query = '''
            CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author_id INTEGER,
                    genre_id INTEGER,
                    is_read INTEGER DEFAULT 0,
                    FOREIGN KEY (author_id) REFERENCES authors(author_id),
                    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
                    )
        '''
        self.db.execute_query(query)
    
    def add_book(self, title: str, author_id: int, genre_id: int) -> None:
        query = "INSERT INTO books (title, author_id, genre_id) VALUES (?, ?, ?)"
        self.db.execute_query(query, title, author_id, genre_id)
    
    def get_last_book(self) -> BookInfo:
        query = '''
            SELECT book_id, title,
            a.author_id, name_author,
            g.genre_id, name_genre,
            is_read
            FROM books b
            JOIN authors a ON b.author_id = a.author_id
            JOIN genres g ON b.genre_id = g.genre_id
            ORDER BY book_id DESC
            LIMIT 1
        '''
        books = self.db.execute_get_data(query)
        book = [BookInfo(*row) for row in books]
        return book[0]
    
    def get_books(self) -> list[BookInfo]:
        query = '''
            SELECT book_id, title,
            a.author_id, name_author,
            g.genre_id, name_genre,
            is_read
            FROM books b
            JOIN authors a ON b.author_id = a.author_id
            JOIN genres g ON b.genre_id = g.genre_id
        '''
        books = self.db.execute_get_data(query)
        books_list = [BookInfo(*row) for row in books]
        return books_list
    
    def mark_as_read(self, book_id: int) -> None:
        query = "UPDATE books SET is_read = 1 WHERE book_id = ?"
        self.db.execute_query(query, book_id)
    
    def get_book_by_id(self, book_id: int) -> Book:
        res = self.db.execute_get_data("SELECT * FROM books WHERE book_id = ?", book_id)
        book_l = [Book(*row) for row in res]
        book: Book = book_l[0]
        return book
    
    def find_books(self, **filters: dict) -> list:
        # поиск книг по названию, автору или жанру
        query = '''
            SELECT book_id, title,
            a.author_id, name_author,
            g.genre_id, name_genre,
            is_read
            FROM books b
            JOIN authors a ON b.author_id = a.author_id
            JOIN genres g ON b.genre_id = g.genre_id
            WHERE
        '''

        key, value = next(iter(filters.items()))
        query += f" {key} LIKE ?"        
        param = f"%{value}%"

        books = self.db.execute_get_data(query, param)
        books_list = [BookInfo(*row) for row in books]
        return books_list
    
    def check_book_id(self, book_id: int) -> bool:
        # проверка наличия книги в базе по переданному id
        query = "SELECT COUNT(*) FROM books WHERE book_id = ?"
        res = self.db.get_int(query, book_id)
        if res == 1:
            return True
        return False
    