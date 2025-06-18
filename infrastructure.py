import sqlite3
from core_interfaces import Book, Author, Genre, BookInfo, BooksLib, AuthorsLib, GenresLib

class DBConnectMethods():
# содержит метода для подключения к БД и передачи запроса

    def __init__(self, db: str):
        self.db = db
        
    def _execute_query(self, query: str, *args) -> None:
    # подключение к БД, выполнение запроса и отключение
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query, args)
        self.conn.commit()
        self.conn.close()

    def _execute_get_data(self, query: str, *args) -> list:
    # подключение к БД, выполнение запроса и возвращение результата запроса
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query, args)
        result: list = self.cursor.fetchall()
        self.conn.close()
        return result
    
    def _get_int(self, query: str, *args) -> int:
    # подключение к БД, выполнение запроса, предпологающего возврат результата int
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        self.cursor.execute(query, args)
        result: tuple = self.cursor.fetchone()
        self.conn.close()
        return result[0]


class AuthorsRepo(AuthorsLib):
# содержит методы для хранения и обработки данных об авторах

    def __init__(self, DBConnectMethods):
    # иниуциализация БД и создание таблицы с авторами
        #self.__init__(db)
        self.db = DBConnectMethods
        query: str = '''
            CREATE TABLE IF NOT EXISTS authors (
                    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_author TEXT UNIQUE
                    )
        '''
        self.db._execute_query(query)

    def add_author(self, name_author: str) -> Author:
    #добавление автора в таблицу authors
        query: str = " INSERT INTO authors (name_author) VALUES (?) "
        self.db._execute_query(query, name_author)
        author_id: int = self.db._get_int(" SELECT last_insert_rowid() FROM authors")
        return Author(author_id, name_author)

    def get_authors(self) -> list[Author]:
    # получение списка всех авторов
        query: str = " SELECT author_id, name_author FROM authors "
        authors: list = self.db._execute_get_data(query)
        authors_list: list = [Author(*row) for row in authors]
        return authors_list
    
    def check_author_id(self, author_id: int) -> bool:
    # проверка наличия автора в базе по переданному id
        query = " SELECT COUNT(*) FROM authors WHERE author_id = ? "
        res: int = self.db._get_int(query, author_id)
        if res == 1:
            return True
        return False
    
    def check_name_author(self, name_author: str) -> bool:
     # проверка наличия автора в базе по имени
        query: str = " SELECT COUNT(*) FROM authors WHERE name_author = ? "
        res: int = self.db._get_int(query, name_author)
        if res == 1:
            return True
        return False


class GenresRepo(GenresLib):
# содержит методы для хранения и обработки данных о жанрах

    def __init__(self, DBConnectMethods):
    # иниуциализация БД и создание таблицы с жанрами
        self.db = DBConnectMethods
        query: str = '''
            CREATE TABLE IF NOT EXISTS genres (
                    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_genre TEXT UNIQUE
                    )
        '''
        self.db._execute_query(query)

    def add_genre(self, name_genre: str) -> Genre:
    #добавление жанра в таблицу genres
        query: str = " INSERT INTO genres (name_genre) VALUES (?)"
        self.db._execute_query(query, name_genre)
        genre_id: int = self.db._get_int(" SELECT last_insert_rowid() FROM genres")
        return Genre(genre_id, name_genre)

    def get_genres(self) -> list[Genre]:
    # получение списка всех авторах
        query: str = " SELECT genre_id, name_genre FROM genres "
        genres: list = self.db._execute_get_data(query)
        genres_list: list = [Genre(*row) for row in genres]
        return genres_list
    
    def check_genre_id(self, genre_id: int) -> bool:
    # проверка наличия жанра в базе по переданному id
        query: str = " SELECT COUNT(*) FROM genres WHERE genre_id = ? "
        res: int = self.db._get_int(query, genre_id)
        if res == 1:
            return True
        return False
    
    def check_name_genre(self, name_genre: str) -> bool:
     # проверка наличия жанра в базе по названию
        query: str = " SELECT COUNT(*) FROM genres WHERE name_genre = ? "
        res: int = self.db._get_int(query, name_genre)
        if res == 1:
            return True
        return False

class BooksRepo(BooksLib):
# содержит методы для хранения и обработки данных о книгах
   
    def __init__(self, DBConnectMethods):
    # иниуциализация БД и создание таблицы с книгами
        self.db = DBConnectMethods
        query: str = '''
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
        self.db._execute_query(query)
    
    def add_book(self, title: str, author_id: int, genre_id: int) -> BookInfo:
    #добавление книги в таблицу books
        query: str = " INSERT INTO books (title, author_id, genre_id) VALUES (?, ?, ?)"
        self.db._execute_query(query, title, author_id, genre_id)
        book_id: int = self.db._get_int(" SELECT MAX(book_id) FROM books")
        b_query: str = '''
            SELECT book_id, title,
            a.author_id, name_author,
            g.genre_id, name_genre,
            is_read
            FROM books b
            JOIN authors a ON b.author_id = a.author_id
            JOIN genres g ON b.genre_id = g.genre_id
            WHERE book_id = ?
        '''
        books = self.db._execute_get_data(b_query, book_id)
        book: BookInfo = books[0]
        return book
    
    def get_books(self) -> list[BookInfo]:
    # получение списка всех книг
        query: str = '''
            SELECT book_id, title,
            a.author_id, name_author,
            g.genre_id, name_genre,
            is_read
            FROM books b
            JOIN authors a ON b.author_id = a.author_id
            JOIN genres g ON b.genre_id = g.genre_id
        '''
        books: list = self.db._execute_get_data(query)
        books_list: list[BookInfo] = [BookInfo(*row) for row in books]
        return books_list
    
    def mark_as_read(self, book_id: int) -> Book:
    # отметка книги как прочитанной
        query: str = " UPDATE books SET is_read = 1 WHERE book_id = ? "
        self.db._execute_query(query, book_id)
        res = self.db._execute_get_data(" SELECT * FROM books WHERE book_id = ? ", book_id)
        book_l: list = [Book(*row) for row in res]
        book: Book = book_l[0]
        return book
    
    def find_books(self, **filters) -> list:
    # поиск книг по названию, автору или жанру
        query: str = '''
            SELECT book_id, title,
            a.author_id, name_author,
            g.genre_id, name_genre,
            is_read
            FROM books b
            JOIN authors a ON b.author_id = a.author_id
            JOIN genres g ON b.genre_id = g.genre_id
            WHERE
        '''
        key = next(iter(filters))
        value = filters[key]
        if key == "title":
            query += " title LIKE ?"
        elif key == "name_author":
            query += " name_author LIKE ?"
        elif key == "name_genre":
            query += " name_genre LIKE ?"
        
        param = f"%{value}%"

        books: list = self.db._execute_get_data(query, param)
        books_list: list[BookInfo] = [BookInfo(*row) for row in books]
        return books_list
    
    def check_book_id(self, book_id: int) -> bool:
    # проверка наличия книги в базе по переданному id
        query = " SELECT COUNT(*) FROM books WHERE book_id = ? "
        res: int = self.db._get_int(query, book_id)
        if res == 1:
            return True
        return False
    