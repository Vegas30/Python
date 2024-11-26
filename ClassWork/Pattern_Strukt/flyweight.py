class Flyweight:
    """Летучий объект, который хранит общее состояние."""

    def __init__(self, shared_state):
        self.shared_state = shared_state  # Внутреннее состояние

    def operation(self, unique_state):
        """Использует внешнее состояние."""
        print(f"Общий состояние: {self.shared_state}, уникальное состояние: {unique_state}")


class FlyweightFactory:
    """Фабрика для управления летучими объектами."""

    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, shared_state):
        """Возвращает существующий объект или создаёт новый."""
        if shared_state not in self._flyweights:
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]

    # Пример использования


factory = FlyweightFactory()

# Создаём несколько летучих объектов с общим состоянием
flyweight1 = factory.get_flyweight("Общий Стейт 1")
flyweight2 = factory.get_flyweight("Общий Стейт 2")

# Применяем уникальное состояние
flyweight1.operation("Уникальное состояние A")
flyweight2.operation("Уникальное состояние B")
flyweight1.operation("Уникальное состояние C")