from core_interfaces import BooksLib, AuthorsLib, GenresLib
from core_realizations import LibRepository
from tabulate import tabulate

class LibInterface():
    def __init__(self, lib_repo: LibRepository):
        self.library = lib_repo

    def _check_input(self) -> int:
    # проверка введенного пользователем числа
        while True:
            try:
                number = int(input())
                return number
            except ValueError:
                print("Ошибка. Введите целое число ")

    def _get_num(self) -> str:
    # получение числа от пользователя (выбранный пункт меню)
        print("\nВведите число, соответствующее выбранному пункту меню:\n")
        self.number = self._check_input()
        return str(self.number)
    
    def _get_title(self) -> str:
    # получение названия книги от пользователя
        while True:
                self.title: str = input("Введите название книги: ")
                if self.title:
                    return self.title
                else:
                    print("Название не может быть пустым. Попробуйте еще раз: ")

    def _get_author(self) -> str:
    # получение нового автора от пользователя            
        while True:
                self.author: str = input("Введите Фамилию и инициалы или псевдоним автора: ")
                if self.author:
                    return self.author
                else:
                    print("Имя не может быть пустым. Попробуйте еще раз: ")

    def _get_genre(self) -> str:
    # получение названия книги от пользователя
        while True:
                self.genre: str = input("Введите название жанра: ")
                if self.genre:
                    return self.genre
                else:
                    print("Название жанра не может быть пустым. Попробуйте еще раз: ")

    def _get_id(self) -> int:
    # получение id от пользователя
        print("Введите id:\n")
        self.id: int = self._check_input()
        return self.id
    
    def _show_books_list(self) -> None:
    # получение списка всех книг
        books: list = self.library.get_books()
        if not books:
            print(" Данные о книгах отсутствуют")
            return
        print(" Список всех книг:")
        headers: list = ["ID", "Название", "Автор", "Жанр", "Прочитано"]
        rows: list = []
        for book in books:
            rows.append([book.book_id, book.title, book.author, book.genre,
                         "Да" if book.is_read else "Нет"])
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def _show_authors_list(self) -> None:
    # получение списка всех авторов
        authors: list = self.library.get_authors()
        if not authors:
            print(" Данные об авторах отсутствуют")
            return
        print(" Список всех авторов:")
        headers: list = ["ID", "Автор"]
        rows: list = []
        for author in authors:
            rows.append([author.author_id, author.name_author])
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def _show_genres_list(self) -> None:
    # получение списка всех жанров
        genres: list = self.library.get_genres()
        if not genres:
            print(" Данные о жанрах отсутствуют")
            return
        print(" Список всех жанров:")
        headers: list = ["ID", "Жанр"]
        rows: list = []
        for genre in genres:
            rows.append([genre.genre_id, genre.name_genre])
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def _find_books(self, **filters) -> None:
        books: list = self.library.find_books(**filters)
        if not books:
            print(" По вашему запросу ни одной книги не найдено")
            return
        print(" Результаты поиска:")
        headers: list = ["ID", "Название", "Автор", "Жанр", "Прочитано"]
        rows: list = []
        for book in books:
            rows.append([book.book_id, book.title, book.author, book.genre,
                         "Да" if book.is_read else "Нет"])
        print(tabulate(rows, headers=headers, tablefmt="grid"))
         
    def run(self) -> None:
    # выводит меню пользователю и вызывает соответствующие функции ядра и инфраструктуры
        print("Добро пожаловать в библиотеку!")
        print("Выберите нужный раздел меню:")
        print("1. Показать список всех книги")
        print("2. Показать список всех авторов")
        print("3. Показать список всех жанров")
        print("4. Искать книги по названию")
        print("5. Искать книги по автору")
        print("6. Искать книги по жанру")
        print("7. Отметить книгу как прочитанную")
        print("8. Добавить новую книгу")
        print("9. Добавить нового автора")
        print("10. Добавить новый жанр")
        print("11. Показать список рекомендуемых к прочтению книг")
        print("0. Выйти")
        while True:
            choice = self.get_num()
            match choice:
                case '1':
                    pass
                case '2':
                    pass
                case '3':
                    pass
                case '4':
                    title = self.get_title()
                    pass
                case '5':
                    author = self.get_author()
                    pass
                case '6':
                    genre = self.get_genre()
                    pass
                case '7':
                    pass
                case '8':
                    title = self.get_title()
                    pass
                case '9':
                    author = self.get_author()
                    pass
                case '10':
                    genre = self.get_genre()
                    pass
                case '11':
                    pass
                case '0':
                    break
                case _:
                    print("Раздел с введенным номером не найден")