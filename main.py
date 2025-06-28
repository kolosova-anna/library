from infrastructure import DBConnectMethods, AuthorsRepo, GenresRepo, BooksRepo
from core_realizations import UnitOfWork, BookService, AuthorsService, GenresService, Recomendations
from ui import LibScreen


def main():
    db = "lib.db"
    conn = DBConnectMethods(db)
    authors_repo = AuthorsRepo(conn)
    genres_repo = GenresRepo(conn)
    books_repo = BooksRepo(conn)
    uow = UnitOfWork(books_repo, authors_repo, genres_repo)
    b_lib = BookService(uow)
    a_lib = AuthorsService(uow)
    g_lib = GenresService(uow)
    rec = Recomendations(uow)
    ui = LibScreen(b_lib, a_lib, g_lib, rec)
    ui.run()
    conn.close()

if __name__ == "__main__":
    main()