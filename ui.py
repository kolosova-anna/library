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
                self.title: str = input("\nВведите название книги: ")
                if self.title:
                    return self.title
                else:
                    print("Название не может быть пустым. Попробуйте еще раз: ")

    def _get_author(self) -> str:
    # получение нового автора от пользователя            
        while True:
                self.author: str = input("\nВведите Фамилию и инициалы или псевдоним автора: ")
                if self.author:
                    return self.author
                else:
                    print("Имя не может быть пустым. Попробуйте еще раз: ")

    def _get_genre(self) -> str:
    # получение названия книги от пользователя
        while True:
                self.genre: str = input("\nВведите название жанра: ")
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
            print("\nДанные о книгах отсутствуют.")
            return
        print("\nСписок всех книг:")
        headers: list = ["ID", "Название", "Автор", "Жанр", "Прочитано"]
        rows: list = []
        for book in books:
            rows.append([book.book_id, book.title, book.name_author, book.name_genre,
                         "Да" if book.is_read else "Нет"])
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def _show_authors_list(self) -> None:
    # получение списка всех авторов
        authors: list = self.library.get_authors()
        if not authors:
            print("\nДанные об авторах отсутствуют.")
            return
        print("\nСписок всех авторов:")
        headers: list = ["ID", "Автор"]
        rows: list = []
        for author in authors:
            rows.append([author.author_id, author.name_author])
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def _show_genres_list(self) -> None:
    # получение списка всех жанров
        genres: list = self.library.get_genres()
        if not genres:
            print("\nДанные о жанрах отсутствуют.")
            return
        print("\nСписок всех жанров:")
        headers: list = ["ID", "Жанр"]
        rows: list = []
        for genre in genres:
            rows.append([genre.genre_id, genre.name_genre])
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def _find_books(self, **filters) -> None:
    # поиск книги по одному из вргументов: названию, автору или жанру
        books: list = self.library.find_books(**filters)
        if not books:
            print("\nПо вашему запросу ни одной книги не найдено.")
            return
        print("\nРезультаты поиска:")
        headers: list = ["ID", "Название", "Автор", "Жанр", "Прочитано"]
        rows: list = []
        for book in books:
            rows.append([book.book_id, book.title, book.name_author, book.name_genre,
                         "Да" if book.is_read else "Нет"])
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def _mark_as_read(self, book_id: int) -> None:
    # отметить книгу как прочитанную по id
        check: bool = self.library.check_book_id(book_id)
        if check:
            book = self.library.mark_as_read(book_id)
            print(f"\nКнига '{book.title}' отмечена как прочитанная.")
            return
        print(f"Книга с id {book_id} не найдена.")

    def _add_book(self, title: str, author_id: int, genre_id: int) -> None:
    # добавление новой книги
        check_author: bool = self.library.check_author_id(author_id)
        check_genre: bool = self.library.check_genre_id(genre_id)
        if not check_author:
            print(f"\nПо id {author_id} авторы не найдены. Проверьте id или внесите информацию о новом авторе.")
        if not check_genre:
            print(f"\nПо id {genre_id} жанры не найдено. Проверьте id или внесите информацию о новом жанре.")
        book: list = [self.library.add_book(title, author_id, genre_id)]
        print("\nНовая книга добавлена:")
        headers: list = ["ID", "Название", "Автор", "Жанр", "Прочитано"]
        rows: list = []
        for b in book:
            rows.append([b[0], b[1], b[3], b[5],
                         "Да" if b[6] else "Нет"])
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def _add_author(self, name_author: str) -> None:
    # добавление нового автора
        check = self.library.check_name_author(name_author)
        if not check:
            author = [self.library.add_author(name_author)]
            print("\nДобавлен новый автор:")
            headers: list = ["ID", "Автор"]
            rows: list = []
            for a in author:
                rows.append([a.author_id, a.name_author])
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        print("\nАвтор с таким именем уже есть в списке")

    def _add_genre(self, name_genre: str) -> None:
    # добавление нового жанра
        check = self.library.check_name_genre(name_genre)
        if not check:
            genre = [self.library.add_genre(name_genre)]
            print("\nДобавлен новый жанр:")
            headers: list = ["ID", "Жанр"]
            rows: list = []
            for g in genre:
                rows.append([g.genre_id, g.name_genre])
            print(tabulate(rows, headers=headers, tablefmt="grid"))
        print("\nЖанр с таким названием уже есть в списке")

    def _show_recomendations(self) -> None:
    # просмотр списка рекомендованных к прочтению книг
        books = self.library.get_recomendations()
        if not books:
            print("\nРекомендаций не найдено. Все книги уже прочитаныю")
        print("\nРекомендуемые к прочтению книги:")
        headers: list = ["ID", "Название", "Автор", "Жанр"]
        rows: list = []
        for b in books:
            rows.append([b.book_id, b.title, b.name_author, b.name_genre])
        print(tabulate(rows, headers=headers, tablefmt="grid"))

    def show_menu_main(self) -> None:
    # выводит пользователю основное меню
        print("\n Добро пожаловать в библиотеку!")
        print("\nВведите номер нужного раздела меню:")
        print("1. Книги")
        print("2. Авторы")
        print("3. Жанры")
        print("4. Посмотреть рекомендации")
        print("0. Выйти")

    def show_menu_book(self) -> None:
    # выводит пользователю меню книг
        print("\n Вы перешли в раздел для работы с книгами")
        print("\nВведите номер нужного пункта меню:")
        print("1. Посмотреть список всех книг")
        print("2. Добавить новую книгу")
        print("3. Искать книгу по названию")
        print("4. Искать книгу по автору")
        print("5. Искать книгу по жанру")
        print("6. Отметить книгу как прочитанную")
        print("0. Вернуться в основное меню")

    def show_menu_author(self) -> None:
    # выводит пользователю меню авторов
        print("\n Вы перешли в раздел для работы с авторами")
        print("\nВведите номер нужного пункта меню:")
        print("1. Посмотреть список всех авторов")
        print("2. Добавить нового автора")
        print("0. Вернуться в основное меню")

    def show_menu_genre(self) -> None:
    # выводит пользователю меню жанров
        print("\n  Вы перешли в раздел для работы с жанрами")
        print("\nВведите номер нужного пункта меню:")
        print("1. Посмотреть список всех жанров")
        print("2. Добавить новый жанр")
        print("0. Вернуться в основное меню")

    def run(self) -> None:
    # выводит пользователю основное меню и направляет в нужные разделы
        self.show_menu_main()
        while True:
            choice = self._get_num()
            match choice:
                case '1':
                    self._run_menu_book()
                case '2':
                    self._run_menu_author()
                case '3':
                    self._run_menu_genre()
                case '4':
                    self._show_recomendations()
                    pass
                case '0':
                    print("\nДо свидания!")
                    break
                case _:
                    print("\nРаздел с введенным номером не найден")

    def _run_menu_book(self) -> None:
    # выводит пользователю меню для работы с книгами
        self.show_menu_book()
        while True:
            choice = self._get_num()
            match choice:
                case '1':
                    self._show_books_list()
                    self.show_menu_book()
                case '2':
                    title = self._get_title()
                    print("\nВведите сначала id автора, затем id жанра")
                    self._show_authors_list()
                    author_id = self._get_id()
                    self._show_genres_list()
                    genre_id = self._get_id()
                    self._add_book(title, author_id, genre_id)
                    self.show_menu_book()
                case '3':
                    title = self._get_title()
                    self._find_books(title=title)
                    self.show_menu_book()
                case '4':
                    author = self._get_author()
                    self._find_books(name_author=author)
                    self.show_menu_book()
                case '5':
                    genre = self._get_genre()
                    self._find_books(name_genre=genre)
                    self.show_menu_book()
                case '6':
                    book_id = self._get_id()
                    self._mark_as_read(book_id)
                    self.show_menu_book()
                case '0':
                    self.show_menu_main()
                    break
                case _:
                    print("\nРаздел с введенным номером не найден")

    def _run_menu_author(self) -> None:
    # выводит пользователю меню для работы с авторами
        self.show_menu_author()
        while True:
            choice = self._get_num()
            match choice:
                case '1':
                    self._show_authors_list()
                    self.show_menu_author()
                case '2':
                    author = self._get_author()
                    self._add_author(author)
                    self.show_menu_author()
                case '0':
                    self.show_menu_main()
                    break
                case _:
                    print("\nРаздел с введенным номером не найден")

    def _run_menu_genre(self) -> None:
    # выводит пользователю меню для работы с жанрами
        self.show_menu_genre()
        while True:
            choice = self._get_num()
            match choice:
                case '1':
                    self._show_genres_list()
                    self.show_menu_genre()
                case '2':
                    genre = self._get_genre()
                    self._add_genre(genre)
                    self.show_menu_genre()
                case '0':
                    self.show_menu_main()
                    break
                case _:
                    print("\nРаздел с введенным номером не найден")