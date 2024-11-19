from dataclasses import dataclass, field

class InvalidBookDataError(Exception):
    """Выбрасывается при некорректных данных книги."""
    def __init__(self, message: str):
        super().__init__(message)


@dataclass
class Book:
    title: str
    author: str
    year: int
    copies: int = field(default=1)

    def __post_init__(self):
        """Проверка корректности данных после инициализации."""
        if not self.title or not isinstance(self.title, str):
            raise InvalidBookDataError("Название книги должно быть строкой и не может быть пустым.")
        if not self.author or not isinstance(self.author, str):
            raise InvalidBookDataError("Автор книги должен быть строкой и не может быть пустым.")
        if not (isinstance(self.year, int) and self.year > 0):
            raise InvalidBookDataError("Год издания должен быть положительным числом.")
        if not (isinstance(self.copies, int) and self.copies >= 0):
            raise InvalidBookDataError("Количество копий должно быть неотрицательным числом.")


class Library:
    def __init__(self):
        self._books = []

    @property
    def books(self):
        """Возвращает список книг (инкапсуляция)."""
        return self._books

    @books.setter
    def books(self, book: Book):
        """Добавляет книгу в библиотеку, проверяя её уникальность."""
        if any(b.title == book.title and b.author == book.author for b in self._books):
            raise InvalidBookDataError(f"Книга '{book.title}' уже существует в библиотеке.")
        self._books.append(book)

    @books.deleter
    def books(self):
        """Удаляет все книги из библиотеки."""
        self._books.clear()

    @staticmethod
    def validate_book_data(title: str, author: str, year: int, copies: int) -> bool:
        """Статический метод для проверки данных книги."""
        return all([
            isinstance(title, str) and title,
            isinstance(author, str) and author,
            isinstance(year, int) and year > 0,
            isinstance(copies, int) and copies >= 0
        ])

    @classmethod
    def create_book_from_string(cls, book_string: str) -> Book:
        """Классовый метод для создания книги из строки."""
        try:
            title, author, year, copies = book_string.split(", ")
            return Book(title, author, int(year), int(copies))
        except ValueError:
            raise InvalidBookDataError("Некорректный формат строки. Используйте: 'Название, Автор, Год, Копии'.")

    def __str__(self):
        """Возвращает строковое представление библиотеки."""
        return f"В библиотеке {len(self._books)} книг."

if __name__ == '__main__':
    library = Library()

    try:
        library.books = Book("1984", "George Orwell", 1949, 5)
        library.books = Book("Brave New World", "Aldous Huxley", 1932, 3)
    except InvalidBookDataError as e:
        print(f"Ошибка добавления книги: {e}")

    print(library)

    try:
        new_book = Library.create_book_from_string("Fahrenheit 451, Ray Bradbury, 1953, 4")
        library.books = new_book
    except InvalidBookDataError as e:
        print(f"Ошибка: {e}")

    for book in library.books:
        print(book.__dict__)

    del library.books
    print(f"После удаления: {library}")

    print("MRO для класса Library:")
    print(Library.__mro__)
