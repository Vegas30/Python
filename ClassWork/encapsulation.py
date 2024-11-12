# Создайте класс Student, представляющий студента. Класс должен иметь:
#
# Скрытый атрибут __grades для хранения списка оценок.
# Методы add_grade для добавления новой оценки и get_average для расчета среднего балла.
# class StudentError(Exception):
#     def __init__(self, value, message):
#         self.value = value
#         self.message = message
#         super().__init__(self.message)
#
#     def __str__(self):
#         return f"Значение {self.value} {self.message}"
#
# def validate_value(value):
#     if not(0 <= value <= 100):
#         raise StudentError(value, "Оценка не входит в диапазон от 1 до 100")
#     return None
#
# class Student:
#     def __init__(self, name):
#         self.__grades = []
#
#     def get_average(self):
#         if self.__grades:
#             return (sum(self.__grades) / len(self.__grades))
#         else:
#             return 0
#
#     def add_grade(self, value):
#         try:
#             validate_value(value)
#             self.__grades.append(value)
#             print(f"Добавлена оценка: {value}")
#         except StudentError as e:
#             print("Ошибка!", e)
#
# def main():
#     student = Student("Сергей")
#     student.add_grade(22)
#     student.add_grade(101)
#     student.add_grade(95)
#     print(f"Средний балл: {student.get_average()}")
# main()


class StudentError(Exception):
    def __init__(self, value, message):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"Значение {self.value} {self.message}"


def validate_value(value):
    if not (0 <= value <= 100):
        raise StudentError(value, "Оценка не входит в диапазон от 1 до 100")
    return None


class Student:
    def __init__(self, name):
        self.__grades = []

    @property
    def grades(self):
        if self.__grades:
            return (sum(self.__grades) / len(self.__grades))
        else:
            return 0

    @grades.setter
    def grades(self, value):
        try:
            validate_value(value)
            self.__grades.append(value)
            print(f"Добавлена оценка: {value}")
        except StudentError as e:
            print("Ошибка!", e)


def main():
    student = Student("Сергей")
    student.grades = 22
    student.grades = 105
    student.grades = 100
    print(f"Средний балл: {student.grades}")


main()


# Два класса: Library, представляющий библиотеку, и Book, представляющий книгу. Библиотека будет содержать список книг, добавленных в нее.
#
# Требования:
#
# Класс Book должен иметь скрытые атрибуты title, author и year.
# Класс Library будет содержать список книг, а также методы для добавления и удаления книг.
# Будем использовать @property для инкапсуляции атрибутов Book.

# class Book:
#     def __init__(self, title, author, year):
#         self.__title = title
#         self.__author = author
#         self.__year = year
#
#     @property
#     def title(self):
#         return self.__title
#
#     @property
#     def author(self):
#         return self.__author
#
#     @property
#     def year(self):
#         return self.__year
#
#     def __str__(self):
#         return f"{self.title}, {self.__author}, {self.year}"
#
# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.__books = []
#
#     def add_book(self, book):
#         if isinstance(book, Book):
#             self.__books.append(book)
#             print(f"Книга {book.title} от автора {book.author} издания {book.year} добавлена в библиотеку")
#         else:
#             print("ЭТО НЕ КНИГА!")
#         return
#
#     def remove_book(self, book_title):
#         for book in self.__books:
#             if book.title == book_title:
#                 self.__books.remove(book)
#                 print("Книга была утилизирована")
#                 return
#         print("Книга была спасена от утилизации. Ее нет в наличии")
#
#
#     def output_list_books(self):
#         if self.__books:
#             print(f"Книги в библиотеки {self.name}")
#             for book in self.__books:
#                 print(f" - {book}")
#
# def main():
#     book1 = Book("Преступление и наказание", "Достоевский", 2023)
#     book2 = Book("Война и мир", "Толстой", 2022)
#
#     library1 = Library("Библиотека Классики")
#
#     library1.add_book(book1)
#     library1.add_book(book2)
#
#     library1.output_list_books()
#
#     library1.remove_book("Война и мир")
#
#     library1.output_list_books()
#
# main()


class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year

    @property
    def title(self):
        return self.__title

    @property
    def author(self):
        return self.__author

    @property
    def year(self):
        return self.__year

    def __str__(self):
        return f"{self.title}, {self.__author}, {self.year}"


class Library:
    def __init__(self, name):
        self.name = name
        self.__books = []

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
            print(f"Книга {book.title} от автора {book.author} издания {book.year} добавлена в библиотеку")
        else:
            print("ЭТО НЕ КНИГА!")
        return

    def remove_book(self, book_title):
        for book in self.__books:
            if book.title == book_title:
                self.__books.remove(book)
                print("Книга была утилизирована")
                return
        print("Книга была спасена от утилизации. Ее нет в наличии")

    def output_list_books(self):
        if self.__books:
            print(f"Книги в библиотеки {self.name}")
            for book in self.__books:
                print(f" - {book}")


def main():
    book1 = Book("Преступление и наказание", "Достоевский", 2023)
    book2 = Book("Война и мир", "Толстой", 2022)

    library1 = Library("Библиотека Классики")

    library1.books = book1
    library1.books = book2

    library1.output_list_books()

    library1.remove_book("Война и мир")

    library1.output_list_books()


if __name__ == '__main__':
    main()
