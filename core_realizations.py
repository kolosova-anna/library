from core_interfaces import Book, Author, Genre, BooksLib, AuthorsLib, GenresLib

class LibRepository(BooksLib):
    # реализация методов для работы с книгами
    def __init__(self, books_lib: BooksLib, authors_lib: AuthorsLib, genres_lib: GenresLib):
        self.books_lib = books_lib
        self.authors_lib = authors_lib
        self.genres_lib = genres_lib

# методы для работы с книгами
    def get_books(self) -> list[Book]:
    # получение списка всех книг в библиотеке
        return self.books_lib.get_books()

    def add_book(self, title: str, author_id: int, genre_id: int) -> Book:
    # добавление новой книги
        return self.books_lib.add_book(title, author_id, genre_id)

    def mark_as_read(self, book_id: int) -> Book:
    # отметка книги как прочитанной
        return self.books_lib.mark_as_read(book_id)
    
    def find_books(self, **filters) -> list[Book]:
    # поиск книг по названию ,автору или жанру
        return self.books_lib.find_books(**filters)
    
# методы для работы с авторами
    def add_author(self, name_author: Author) -> Author:
    # добавление нового автора
        return self.authors_lib.add_author(name_author)
    
    def get_authors(self) -> list[Author]:
    # получение списка всех авторов
        return self.authors_lib.get_authors()

# методы для работы с жанрами    
    def add_genre(self, name_genre: Genre) -> Genre:
    # добавление нового жанра
        return self.genres_lib.add_genre(name_genre)
    
    def get_genres(self) -> list[Genre]:
    # получение списка всех жанров
        return self.genres_lib.get_genres()
    
# рекомендации
    def get_recomendations(self) -> list[Book]:
        books_list = self.books_lib.get_books()
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