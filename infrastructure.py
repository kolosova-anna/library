import sqlite3

class Infrastructure():
    # содержит методы для хранения и обработки данных

    def __init__(self):
        #инициализация (создание) БД с таблицами
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS authors (
                    author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_author TEXT UNIQUE
                    )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS genres (
                    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name_genre TEXT UNIQUE
                    )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    author_id INTEGER,
                    genre_id INTEGER,
                    FOREIGN KEY (author_id) REFERENCES authors(author_id),
                    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
                    )
        ''')
        self.conn.commit()
        self.conn.close()

    def add_author(self, author: str) -> None:
        #добавление автора в таблицу authors
        self.conn = sqlite3.connect('library.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute(" INSERT INTO authors (name_author) VALUES (?)", (author,))
        self.conn.commit()
        self.conn.close()