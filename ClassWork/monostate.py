# Monostate
class Monostate:
    _shared_state = {}  # Общий словарь состояния


    def __init__(self):
        self.__dict__ = self._shared_state  # Перенаправление на общий словарь


obj1 = Monostate()
obj2 = Monostate()


obj1.name = "Object 1"
print(obj2.name)  # "Object 1" — состояние разделяется


obj2.name = "Object 2"
print(obj1.name)  # "Object 2" — изменение в одном объекте влияет на другой