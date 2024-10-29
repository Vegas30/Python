# Задача 1: Перегрузка операторов сложения и вычитания
# Описание:
# Создайте класс Vector, который будет представлять вектор в двумерном
# пространстве. Реализуйте магические методы __add__ и __sub__ для
# сложения и вычитания двух векторов.
# Требования:
# ● Реализуйте конструктор __init__, который принимает координаты
# вектора (x, y).
# ● Реализуйте магический метод __add__ для сложения векторов.
# ● Реализуйте магический метод __sub__ для вычитания векторов.
# ● Реализуйте магический метод __repr__ для текстового представления
# вектора.
# Пример использования:
# v1 = Vector(3, 4)
# v2 = Vector(1, 2)
# print(v1 + v2) # Vector(4, 6)
# print(v1 - v2) # Vector(2, 2)

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


def main():
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    print(v1 + v2)  # Vector(4, 6)
    print(v1 - v2)  # Vector(2, 2)


if __name__ == '__main__':
    main()


# Задача 2: Перегрузка оператора сравнения
# Описание:
# Создайте класс Box, который будет представлять коробку с определённым
# объёмом. Реализуйте магические методы сравнения (__eq__, __lt__, __gt__), чтобы сравнивать объёмы коробок.
# Требования:
# ● Реализуйте конструктор __init__, который принимает длину, ширину и высоту коробки.
# ● Реализуйте магический метод __eq__ для проверки равенства объемов.
# ● Реализуйте магические методы __lt__ и __gt__ для сравнения коробок по объему.
# ● Реализуйте магический метод __repr__ для вывода размеров коробки.
# Пример использования:
# b1 = Box(2, 3, 4) # Объем: 24
# b2 = Box(1, 6, 4) # Объем: 24
# b3 = Box(3, 3, 3) # Объем: 27
# print(b1 == b2) # True
# print(b1 < b3) # True
# print(b3 > b2) # True

class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
        self.volume = self.length * self.width * self.height

    # def volume(self):
    #     return self.length * self.width * self.height
    #
    # def __eq__(self, other):
    #     return self.volume() == other.volume()
    def __eq__(self, other):
        if isinstance(other, Box):
            return self.volume == other.volume
        return False

    def __lt__(self, other):
        if isinstance(other, Box):
            return self.volume < other.volume
        return False

    def __gt__(self, other):
        if isinstance(other, Box):
            return self.volume > other.volume
        return False

    def __repr__(self):
        return f"Размеры коробки: длина - {self.length}, ширина - {self.width}, высота - {self.height}"


def main():
    b1 = Box(2, 3, 4)  # Объем: 24
    b2 = Box(1, 6, 4)  # Объем: 24
    b3 = Box(3, 3, 3)  # Объем: 27
    print(b1 == b2)  # True
    print(b1 < b3)  # True
    print(b3 > b2)  # True
    print(b1)


if __name__ == '__main__':
    main()


# Задача 3: Перегрузка методов для строкового представления
# Описание:
# Создайте класс Person, представляющий человека. Реализуйте магические
# методы __str__ и __repr__ для предоставления краткого и подробного
# строкового представления объекта соответственно.
# Требования:
# ● Реализуйте конструктор __init__, принимающий имя и возраст.
# ● Реализуйте магический метод __str__, который возвращает краткое
# описание человека (например, имя).
# ● Реализуйте магический метод __repr__, который возвращает полную
# информацию (имя и возраст) в удобном для разработчиков формате.
# Пример использования:
# p = Person("Alice", 30)
# print(str(p)) # Alice
# print(repr(p)) # Person(name='Alice', age=30)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


def main():
    p = Person("Alice", 30)
    print(str(p))  # Alice
    print(repr(p))  # Person(name='Alice', age=30)


if __name__ == '__main__':
    main()


# Задача 4: Индексация объектов
# Описание:
# Создайте класс Polynomial, представляющий многочлен. Реализуйте
# магический метод __getitem__ для получения коэффициента при степени
# многочлена по индексу.
# Требования:
# ● Реализуйте конструктор __init__, принимающий список коэффициентов.
# ● Реализуйте магический метод __getitem__, который возвращает
# коэффициент при указанной степени многочлена.
# ● Реализуйте магический метод __repr__, чтобы показывать многочлен
# в виде строки.
# Пример использования:
# p = Polynomial([3, 0, 2]) # 3x^2 + 0x + 2
# print(p[0]) # 3 (коэффициент при x^2)
# print(p[2]) # 2 (коэффициент при x^0)

class Polynomial:
    def __init__(self, ratio_list):
        self.ratio_list = ratio_list

    def __getitem__(self, index):
        if index < len(self.ratio_list):
            return self.ratio_list[index]
        else:
            return 0

    def __repr__(self):
        terms = []
        for i, coeff in enumerate(self.ratio_list):
            if coeff != 0:
                if i == 0:
                    terms.append(str(coeff))
                else:
                    terms.append(f"{coeff}x^{i}")
        return "+".join(terms[::-1])


def main():
    p = Polynomial([3, 0, 2])  # 3x^2 + 0x + 2
    print(p[2])  # 3 (коэффициент при x^2)
    print(p[0])  # 2 (коэффициент при x^0)


if __name__ == '__main__':
    main()


# Задача 5: Итерация по объектам
# Описание:
# Создайте класс Fibonacci, который генерирует числа Фибоначчи до
# определённого предела. Реализуйте магические методы __iter__ и
# __next__, чтобы объект этого класса был итерируемым.
# Требования:
# ● Реализуйте конструктор __init__, который принимает максимальное
# количество чисел Фибоначчи.
# ● Реализуйте магический метод __iter__, который возвращает
# итератор.
# ● Реализуйте магический метод __next__, который возвращает
# следующее число Фибоначчи до достижения предела.
# Пример использования:
# fib = Fibonacci(5)
# for num in fib:
# print(num) # 0 1 1 2 3
class Fibonacci:
    def __init__(self, max_count):
        self.max_count = max_count

    def __iter__(self):
        return self

    def __next__(self):
        pass


def main():
    fib = Fibonacci(5)
    for num in fib:
        print(num)  # 0 1 1 2 3


if __name__ == '__main__':
    main()

# Задачи на методы класса.
# ------------------------
# Задача 1: Подсчет созданных объектов
# Описание:
# Создайте Book метод класса, который будет отслеживать количество
# созданных объектов этого класса.
# Требования:
# ● Реализуйте атрибут класса book_count, который будет хранить
# количество созданных объектов.
# ● Реализуйте конструктор __init__, который увеличивает счётчик при
# каждом создании нового объекта.
# ● Реализуйте классовый метод get_book_count, который возвращает
# текущее количество созданных объектов.
# Пример использования:
# class Book:
# # Реализация класса
# b1 = Book()
# b2 = Book()
# b3 = Book()
# print(Book.get_book_count()) # 3
