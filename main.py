from infrastructure import AuthorsRepo, GenresRepo, BooksRepo
from core_realizations import LibRepository
from ui import LibInterface

def main():
    db = "library.db"
    authors_repo = AuthorsRepo(db)
    genres_repo = GenresRepo(db)
    books_repo = BooksRepo(db)
    library = LibRepository(books_repo, authors_repo, genres_repo)
    ui = LibInterface(library)
    ui.run()

if __name__ == "__main__":
    main()