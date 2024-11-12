# Задача: Управление персоналом в компании
# Условие: Создайте систему управления персоналом в компании, используя ООП.
#
# Создайте абстрактный класс Employee, который будет представлять общие характеристики сотрудников.
# Этот класс должен включать:
#
# Инкапсулированные (приватные) поля для имени и зарплаты сотрудника.
# Абстрактные методы get_role() (для возвращения должности сотрудника) и calculate_bonus()
# (для расчета бонуса в зависимости от должности).
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

from typing import Protocol


class Employee(Protocol):
    def get_role(self):
        pass

    def calculate_bonus(self):
        pass

class BaseClass:
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary

    def display_info(self):
        print(
            f"Имя: {self._name}, Роль: {self.get_role()}, Зарплата: {self._salary}, Bonus: {self.calculate_bonus()}"
        )
class Manager(BaseClass):
    def get_role(self):
        return "Менеджер"

    def calculate_bonus(self):
        return self._salary * 0.15


class Developer(BaseClass):
    def get_role(self):
        return "Разработчик"

    def calculate_bonus(self):
        return self._salary * 0.10

class Designer(BaseClass):
    def get_role(self):
        return "Дизайнер"

    def calculate_bonus(self):
        return self._salary * 0.05

def make_get_role(employee: Employee):
    print(employee.get_role())

employees = [
    Manager("Максим", 80000),
    Developer("Python-41", 100000),
    Designer("Расул", 60000),
]

for employee in employees:
    employee.display_info()
    print()

for employee in employees:
    make_get_role(employee)