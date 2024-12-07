
from abc import ABC, abstractmethod


# Общий интерфейс состояния
class State(ABC):
    @abstractmethod
    def insert_coin(self, context):
        pass


    @abstractmethod
    def select_drink(self, context):
        pass


    @abstractmethod
    def dispense_drink(self, context):
        pass




# Конкретные состояния
class WaitingForCoinState(State):
    def insert_coin(self, context):
        print("Монета принята. Выберите напиток.")
        context.set_state(context.select_drink_state)


    def select_drink(self, context):
        print("Вы не можете выбрать напиток, пока не вставите монету.")


    def dispense_drink(self, context):
        print("Напиток не может быть выдан без оплаты.")




class SelectDrinkState(State):
    def insert_coin(self, context):
        print("Вы уже внесли оплату.")


    def select_drink(self, context):
        print("Напиток выбран. Пожалуйста, подождите.")
        context.set_state(context.dispense_drink_state)


    def dispense_drink(self, context):
        print("Сначала выберите напиток.")




class DispenseDrinkState(State):
    def insert_coin(self, context):
        print("Подождите, напиток уже выдается.")


    def select_drink(self, context):
        print("Напиток уже выдан. Вы не можете выбрать ещё один.")


    def dispense_drink(self, context):
        print("Напиток выдан. Спасибо за покупку!")
        context.set_state(context.waiting_for_coin_state)




class OutOfStockState(State):
    def insert_coin(self, context):
        print("Автомат пуст. Монета возвращена.")


    def select_drink(self, context):
        print("Автомат пуст. Невозможно выбрать напиток.")


    def dispense_drink(self, context):
        print("Автомат пуст. Напитки недоступны.")




# Контекст
class VendingMachine:
    def __init__(self):
        self.waiting_for_coin_state = WaitingForCoinState()
        self.select_drink_state = SelectDrinkState()
        self.dispense_drink_state = DispenseDrinkState()
        self.out_of_stock_state = OutOfStockState()


        self.state = self.waiting_for_coin_state


    def set_state(self, state):
        self.state = state


    def insert_coin(self):
        self.state.insert_coin(self)


    def select_drink(self):
        self.state.select_drink(self)


    def dispense_drink(self):
        self.state.dispense_drink(self)




# Клиентский код
if __name__ == "__main__":
    machine = VendingMachine()


    # Цикл работы автомата
    machine.insert_coin()
    machine.select_drink()
    machine.dispense_drink()


    # Попытка вставить монету ещё раз
    machine.insert_coin()

