from infrastructure import DBConnectMethods, AuthorsRepo, GenresRepo, BooksRepo
from core_realizations import LibRepository
from ui import LibInterface

def main():
    db = "library.db"
    conn = DBConnectMethods(db)
    authors_repo = AuthorsRepo()
    genres_repo = GenresRepo()
    books_repo = BooksRepo()
    library = LibRepository(books_repo, authors_repo, genres_repo)
    ui = LibInterface(library)
    ui.run()

if __name__ == "__main__":
    main()