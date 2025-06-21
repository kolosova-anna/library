from infrastructure import DBConnectMethods, AuthorsRepo, GenresRepo, BooksRepo
from core_realizations import LibService
from ui import LibInterface


def main():
    db = "lib.db"
    conn = DBConnectMethods(db)
    authors_repo = AuthorsRepo(conn)
    genres_repo = GenresRepo(conn)
    books_repo = BooksRepo(conn)
    library = LibService(books_repo, authors_repo, genres_repo)
    ui = LibInterface(library)
    ui.run()

if __name__ == "__main__":
    main()