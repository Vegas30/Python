# 1. Создайте класс Student, который хранит информацию о каждом студенте (имя и
# оценки по предметам). Реализуйте метод класса для получения кол-во студентов и
# метод для вычисления среднего балла по всем студентам.

class Student:
    students = []

    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
        Student.students.append(self)

    def average_grades(self):
        return sum(self.grades) / len(self.grades)

    @classmethod
    def total_students(cls):
        return len(cls.students)

    @classmethod
    def total_average_students(cls):
        total_grades = sum(sum(student.grades) for student in cls.students)
        total_len = sum(len(student.grades) for student in cls.students)
        return total_grades / total_len


def main():
    s1 = Student("Максим", [56, 44, 95, 56])
    s2 = Student("Анастасия", [90, 90, 90, 100])
    print(s1.average_grades())
    total_students = Student.total_students()
    total_grades = Student.total_average_students()
    print(total_grades)


if __name__ == "__main__":
    main()


# 2. Создайте класс Car, который хранит марку и модель автомобиля, а также имеет
# метод класса для подсчета общего кол-ва созданных автомобилей.

class Car:
    count = 0

    def __init__(self, marka, model):
        self.marka = marka
        self.model = model
        Car.count += 1

    @classmethod
    def get_total_cars(cls):
        return cls.count


def main():
    s1 = Car("Максим", "8865")
    s2 = Car("Анастасия", "good")
    print(Car.get_total_cars())


if __name__ == "__main__":
    main()


# Создайте класс Rectangle, который может быть создан двумя способами:
# либо по длине и ширине, либо по одной стороне, если это квадрат. Используйте
# метод класса для создания объекта через длину квадрата.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    @classmethod
    def square(cls, side_length):
        return cls(side_length, side_length)


def main():
    s1 = Rectangle(4, 5)
    s2 = Rectangle.square(4)
    print(s1.width, s2.width)


if __name__ == "__main__":
    main()


# 4. Создайте класс Product, который имеет уникальный номер для каждого товара.
# Реализуйте метод класса для создания товара с уникальным номером.
class Product:
    id_count = 0
    products = []

    def __init__(self, name):
        self.name = name
        Product.id_count += 1
        self.product_id = Product.id_count
        Product.products.append(self)

    @classmethod
    def podgotovka_init(cls):
        name = input("Введите имя товара: ")
        return cls(name)

    @classmethod
    def output_product(cls):
        for product in cls.products:
            print(f"id:{product.product_id} - {product.name}")


def main():
    for _ in range(5):
        Product.podgotovka_init()
    Product.output_product()


if __name__ == "__main__":
    main()


# Создайте класс Employee, который содержит информация о сотрудниках компании
# (имя и зарплата). Реализуйте метод класса для повышения зарплат на заданный процент

class Employee:
    employees = []

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employees.append(self)

    @classmethod
    def salary_all_persent(cls, percent):
        for salara in cls.employees:
            salara.salary += salara.salary * (percent / 100)

    def __str__(self):
        return f"Сотрудник {self.name} стал зарабатывать {self.salary}"


def main():
    s1 = Employee("Максим", 4800)
    s2 = Employee("Максим (по черному рынку)", 999999999)
    Employee.salary_all_persent(10)
    print(s1, s2)


if __name__ == "__main__":
    main()
