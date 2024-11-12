# Условие: Создайте абстрактный класс Vehicle с абстрактными методами start_engine и stop_engine.
# Затем создайте подклассы Car и Motorcycle, которые реализуют эти методы.
#
# Требования:
#
# Метод start_engine должен выводить сообщение о запуске двигателя.
# Метод stop_engine должен выводить сообщение об остановке двигателя.

from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start_engine(self) -> None:
#         pass
#
#     @abstractmethod
#     def stop_engine(self) -> None:
#         pass
#
# class Car(Vehicle):
#     def __init__(self, model):
#         self.model = model
#
#     def start_engine(self) -> None:
#         print("Двигатель автомобиля запущен")
#
#     def stop_engine(self) -> None:
#         print("Двигатель автомобиля выключен")
#
# car = Car("Toyota")
#
# car.start_engine()
# car.stop_engine()

from typing import Protocol
class Vehicle(Protocol):
    def start_engine(self) -> None:
        pass

    def stop_engine(self) -> None:
        pass
class Car:
    def __init__(self, model):
        self.model = model

    def start_engine(self) -> None:
        print("Двигатель автомобиля запущен")

    def stop_engine(self) -> None:
        print("ff")

def make_start_stop(vehicle: Vehicle):
    vehicle.start_engine()
    vehicle.stop_engine()

car = Car("Toyota")
make_start_stop(car)

# Задача: Управление персоналом в компании
# Условие: Создайте систему управления персоналом в компании, используя ООП.
#
# Создайте абстрактный класс Employee, который будет представлять общие характеристики сотрудников.
# Этот класс должен включать:
#
# Инкапсулированные (приватные) поля для имени и зарплаты сотрудника.
# Абстрактные методы get_role() (для возвращения должности сотрудника) и calculate_bonus() (для расчета бонуса
# в зависимости от должности).
# Метод для отображения информации о сотруднике.
# Реализуйте несколько подклассов для конкретных ролей сотрудников:
#
# Manager (Менеджер): получает бонус в размере 15% от зарплаты.
# Developer (Разработчик): получает бонус в размере 10% от зарплаты.
# Designer (Дизайнер): получает бонус в размере 5% от зарплаты.
# Используйте полиморфизм, чтобы создать список сотрудников, в котором каждый объект вызывает свои собственные
# реализации метода calculate_bonus() и get_role().
#
# Инкапсуляция обеспечит скрытие деталей зарплаты и других данных сотрудников, чтобы доступ к ним можно было
# осуществить только через методы класса.


from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def calculate_bonus(self):
        pass

    def display_info(self):
        print(
            f"Имя: {self._name}, Роль: {self.get_role()}, Зарплата: {self._salary}, Bonus: {self.calculate_bonus()}"
        )


class Manager(Employee):
    def get_role(self):
        return "Менеджер"

    def calculate_bonus(self):
        return self._salary * 0.15


class Developer(Employee):
    def get_role(self):
        return "Разработчик"

    def calculate_bonus(self):
        return self._salary * 0.10


class Designer(Employee):
    def get_role(self):
        return "Дизайнер"

    def calculate_bonus(self):
        return self._salary * 0.05


employees = [
    Manager("Максим", 80000),
    Developer("Python-41", 100000),
    Designer("Расул", 60000),
]

for employee in employees:
    employee.display_info()
    print()



from abc import ABC, abstractmethod


class Employee(ABC):
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
        self.__password = "root"

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def calculate_bonus(self):
        pass

    @property
    def password(self):
        return self.__password

    def display_info(self):
        print(
            f"Имя: {self._name}, Роль: {self.get_role()}, Зарплата: {self._salary}, Bonus: {self.calculate_bonus()}"
        )


class Manager(Employee):
    def get_role(self):
        return "Менеджер"

    def calculate_bonus(self):
        return self._salary * 0.15

    def get_password(self):
        return self.password


class Developer(Employee):
    def get_role(self):
        return "Разработчик"

    def calculate_bonus(self):
        return self._salary * 0.10


class Designer(Employee):
    def get_role(self):
        return "Дизайнер"

    def calculate_bonus(self):
        return self._salary * 0.05


employees = [
    Manager("Максим", 80000),
    Developer("Python-41", 100000),
    Designer("Расул", 60000),
]

for employee in employees:
    employee.display_info()
    print()

print(employees[0].get_password())
