from abc import ABC, abstractmethod


# Базовый класс с методом-шаблоном
class Beverage(ABC):
    def prepare(self):
        """Шаблонный метод: определяет общий алгоритм"""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Кипячение воды...")

    def pour_in_cup(self):
        print("Наливание напитка в чашку...")

    @abstractmethod
    def brew(self):
        """Шаг, который реализуется в подклассах"""
        pass

    @abstractmethod
    def add_condiments(self):
        """Шаг, который реализуется в подклассах"""
        pass


# Конкретный подкласс для чая
class Tea(Beverage):
    def brew(self):
        print("Заваривание чая...")

    def add_condiments(self):
        print("Добавление лимона...")


# Конкретный подкласс для кофе
class Coffee(Beverage):
    def brew(self):
        print("Заваривание кофе...")

    def add_condiments(self):
        print("Добавление сахара и молока...")


# Клиентский код
if __name__ == "__main__":
    print("Готовим чай:")
    tea = Tea()
    tea.prepare()

    print("\nГотовим кофе:")
    coffee = Coffee()
    coffee.prepare()

# Результат выполнения:
# Готовим чай:
# Кипячение воды...
# Завариваниечая...
# Наливание напитка в чашку...
# Добавление лимона...
#
# Готовим кофе:
# Кипячение воды...
# Заваривание кофе...
# Наливание напитка в чашку...
# Добавление сахара и молока...
