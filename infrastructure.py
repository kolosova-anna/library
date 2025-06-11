import sqlite3
from core_interfaces import Book, Author, Genre, BooksLib, AuthorsLib, GenresLib

class AuthorsRepo(AuthorsLib):
# содержит методы для хранения и обработки данных об авторах

    def __init__(self, db: str):
    # иниуциализация БД и создание таблицы с авторами
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS authors (
                    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_author TEXT UNIQUE
                    )
        ''')
        self.conn.commit()
        self.conn.close()

    def add_author(self, name_author: Author) -> Author:
        #добавление автора в таблицу authors
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        self.cursor.execute(" INSERT INTO authors (name_author) VALUES (?)", (name_author.name_author,))
        self.conn.commit()
        self.conn.close()

class GenresRepo(GenresLib):
# содержит методы для хранения и обработки данных о жанрах

    def __init__(self, db: str):
    # иниуциализация БД и создание таблицы с жанрами
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS genres (
                    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_genre TEXT UNIQUE
                    )
        ''')
        self.conn.commit()
        self.conn.close()


class BooksRepo(BooksLib):
# содержит методы для хранения и обработки данных о книгах
#    
    def __init__(self, db: str):
    # иниуциализация БД и создание таблицы с книгами
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author_id INTEGER,
                    genre_id INTEGER,
                    is_read INTEDER DEFAULT 0
                    FOREIGN KEY (author_id) REFERENCES authors(author_id),
                    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
                    )
        ''')
        self.conn.commit()
        self.conn.close()