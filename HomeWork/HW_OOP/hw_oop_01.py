# Задача 1: Класс «Человек»
# Создайте класс Person, который содержит:
#  - атрибуты: name (имя) и age (возраст),
#  - метод greet(), который выводит сообщение: "Привет, меня зовут <name> и мне <age> лет!".
# 	 Создайте несколько объектов класса и вызовите метод greet() для каждого.
#  Пример использования:
#  person1 = Person("Алексей", 30)
#  person2 = Person("Мария", 25)
#
#  person1.greet()  # Привет, меня зовут Алексей и мне 30 лет!
#  person2.greet()  # Привет, меня зовут Мария и мне 25 лет!
class Person:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Привет, меня зовут {self.name} и мне {self.age}")


# Задача 2: Класс «Прямоугольник»
# Создайте класс Rectangle, который содержит:
#  - атрибуты: width (ширина) и height (высота),
#  - метод area(), который возвращает площадь прямоугольника,
#  - метод perimeter(), который возвращает периметр прямоугольника.
# 	 Создайте несколько объектов класса и выведите площадь и периметр для каждого.
#  Пример использования:
#  rect1 = Rectangle(5, 10)
#  rect2 = Rectangle(7, 3)
#
#  print(rect1.area())  # 50
#  print(rect1.perimeter())  # 30
#  print(rect2.area())  # 21
#  print(rect2.perimeter())  # 20
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


# Задача 3: Класс «Автомобиль»
# Создайте класс Car, который содержит:
# - атрибуты: brand (марка), model (модель), year (год выпуска),
# - метод car_info(), который выводит информацию об автомобиле в
# формате: "Марка: <brand>, Модель: <model>, Год выпуска: <year>".
# Создайте несколько объектов класса и вызовите метод car_info() для
# каждого.
# Пример использования:
# car1 = Car("Toyota", "Corolla", 2020)
# car2 = Car("Ford", "Focus", 2018)
# car1.car_info() # Марка: Toyota, Модель: Corolla, Год выпуска: 2020
# car2.car_info() # Марка: Ford, Модель: Focus, Год выпуска: 2018
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год выпуска: {self.year}")


# Задача 4: Класс «Студент»
# Создайте класс Student, который содержит:
# - атрибуты: name (имя студента) и grades (список оценок),
# - метод average_grade(), который возвращает среднюю оценку студента.
# Создайте несколько объектов класса и выведите среднюю оценку
# для каждого студента.
# Пример использования:
# student1 = Student("Иван", [4, 5, 5, 3])
# student2 = Student("Ольга", [5, 5, 4, 4])
# print(student1.average_grade()) # 4.25
# print(student2.average_grade()) # 4.5
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        return sum(grade for grade in self.grades) / len(self.grades)


# Задача 5: Класс «Кот»
# Создайте класс Cat, который содержит:
# - атрибуты: name (имя кота) и color (цвет),
# - метод meow(), который выводит: "Мяу! Меня зовут <name>, мой цвет —
# <color>".
# Создайте несколько объектов класса и вызовите метод meow() для
# каждого.
# Пример использования:
# cat1 = Cat("Барсик", "рыжий")
# cat2 = Cat("Мурка", "черный")
# cat1.meow() # Мяу! Меня зовут Барсик, мой цвет — рыжий
# cat2.meow() # Мяу! Меня зовут Мурка, мой цвет — черный
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def meow(self):
        print(f"Мяу! Меня зовут {self.name}, мой цвет — {self.color}")


# Задача 6: Класс «Телевизор»
# Создайте класс Television, который содержит:
# - атрибуты: brand (марка) и channel (текущий канал),
# - метод switch_channel(new_channel), который изменяет текущий канал на
# new_channel и выводит сообщение: "Канал переключен на <new_channel>".
# Создайте несколько объектов класса и переключите каналы на
# каждом телевизоре.
# Пример использования:
# tv1 = Television("Samsung", 1)
# tv2 = Television("LG", 5)
# tv1.switch_channel(3) # Канал переключен на 3
# tv2.switch_channel(7) # Канал переключен на 7
class Television:
    def __init__(self, brand, channel):
        self.brand = brand
        self.channel = channel

    def switch_channel(self, new_channel):
        self.channel = new_channel
        print(f"Канал переключен на {self.channel}")
        # print(f"Канал переключен на {new_channel}")


# Задача 7: Взаимодействие классов «Автор» и «Книга»
# Создайте два класса: Author и Book.
# 1. Класс Author содержит:
# - атрибуты: name (имя автора) и age (возраст),
# - метод author_info(), который выводит информацию об авторе в формате:
# "Автор: <name>, Возраст: <age>".
# 2. Класс Book содержит:
# - атрибуты: title (название книги) и author (объект класса Author),
# - метод book_info(), который выводит информацию о книге и её авторе в
# формате: "Книга: <title>, Автор: <name>".
# Создайте несколько объектов класса Author и несколько объектов
# класса Book.
# Выведите информацию о книгах и их авторах.
class Author:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def author_info(self):
        print(f"Автор: {self.name}, Возраст: {self.age}")


class Book:
    def __init__(self, title, author: Author):
        self.title = title
        self.author = author

    def book_info(self):
        print(f"Книга: {self.title}, Автор: {self.author.name}")


def main():
    # Задача 1:
    person1 = Person("Алексей", 30)
    person2 = Person("Мария", 25)

    person1.greet()
    person2.greet()

    # Задача 2:
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(7, 3)

    print(rect1.area())  # 50
    print(rect1.perimeter())  # 30
    print(rect2.area())  # 21
    print(rect2.perimeter())  # 20

    # Задача 3:
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Ford", "Focus", 2018)
    car1.car_info()  # Марка: Toyota, Модель: Corolla, Год выпуска: 2020
    car2.car_info()  # Марка: Ford, Модель: Focus, Год выпуска: 2018

    # Задача 4:
    student1 = Student("Иван", [4, 5, 5, 3])
    student2 = Student("Ольга", [5, 5, 4, 4])
    print(student1.average_grade())  # 4.25
    print(student2.average_grade())  # 4.5

    # Задача 5:
    cat1 = Cat("Барсик", "рыжий")
    cat2 = Cat("Мурка", "черный")
    cat1.meow()  # Мяу! Меня зовут Барсик, мой цвет — рыжий
    cat2.meow()  # Мяу! Меня зовут Мурка, мой цвет — черный

    # Задача 6:
    tv1 = Television("Samsung", 1)
    tv2 = Television("LG", 5)
    tv1.switch_channel(3)  # Канал переключен на 3
    tv2.switch_channel(7)  # Канал переключен на 7

    # Задача 7:

    author1 = Author("Пушкин", 39)
    author2 = Author("Толстой", 45)
    author3 = Author("Гоголь", 31)
    book1 = Book("Евгений Онегин", author1)
    book2 = Book("Война и мир", author2)
    book3 = Book("Мертвые души", author3)

    book1.book_info()
    book2.book_info()
    book3.book_info()


if __name__ == '__main__':
    main()
