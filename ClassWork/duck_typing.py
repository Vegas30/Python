# Создайте класс Employee, представляющий сотрудника с базовой оплатой труда.
# Создайте классы-наследники HourlyEmployee и SalariedEmployee, которые рассчитывают
# зарплату по-разному: по почасовой ставке и фиксированному окладу.
# Добавьте статический метод для подсчета общей зарплаты всех сотрудников.

class Employee:
    total_salary = 0

    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        return 0

    @staticmethod
    def add_to_total(salary):
        Employee.total_salary += salary

    @classmethod
    def get_total_salary(cls):
        return cls.total_salary


class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        self.hour_salary = self.hours_worked * self.hourly_rate
        self.add_to_total(self.hour_salary)
        return self.hour_salary


class SalariedEmployee(Employee):
    def __init__(self, name, mounth_salary=8000):
        super().__init__(name)
        self.mounth_salary = mounth_salary

    def calculate_salary(self):
        self.add_to_total(self.mounth_salary)
        return self.mounth_salary


def main():
    employees = []
    emp1 = HourlyEmployee("Максим", 25, 800)
    emp2 = HourlyEmployee("Алиса", 50, 800)

    emp3 = SalariedEmployee("Иван")
    emp4 = SalariedEmployee("Иван", 12000)

    employees = [emp1, emp2, emp3, emp4]
    for employee in employees:
        print(f"Почасовая ставка сотрудника {employee.name} составляет {employee.calculate_salary()}")

    print(f"Общая зарплата всех сотрудников {Employee.get_total_salary()}")


if __name__ == "__main__":
    main()


# Создайте базовый класс Order, который хранит информацию о заказе.
# Реализуйте метод для расчета суммы заказа с учетом налогов.
# Создайте классы-наследники для различных типов заказов
# (DomesticOrder и InternationalOrder),
# каждый из которых применяет разные налоговые ставки и сборы.
# Реализуйте полиморфный метод для расчета итоговой стоимости.

class Order:
    def __init__(self, amount):
        self.amount = amount

    def total_price(self):
        return self.amount


class DomestricOrder(Order):
    def total_price(self):
        return self.amount * 1.1


class InternationalOrder(Order):
    def total_price(self):
        return self.amount * 1.2 + 15


def main():
    domectic = DomestricOrder(100)
    international = InternationalOrder(100)
    print(domectic.total_price())
    print(international.total_price())


main()
