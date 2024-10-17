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


def main():
    # Задача 1:
    person1 = Person("Алексей", 30)
    person2 = Person("Мария", 25)

    person1.greet()
    person2.greet()

    # Задача 2:


if __name__ == '__main__':
    main()
