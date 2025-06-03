import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS authors (
               author_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name_author TEXT UNIQUE
               )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS genres (
               genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name_genre TEXT UNIQUE
               )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
               book_id INTEGER PRIMARY KEY AUTOINCREMENT,
               title TEXT,
               author_id INTEGER,
               genre_id INTEGER,
               FOREIGN KEY (author_id) REFERENCES authors(author_id),
               FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
               )
''')
conn.commit()
conn.close()
