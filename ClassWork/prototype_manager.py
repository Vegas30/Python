# Prototype Manager
import copy


class Prototype:
    """Базовый класс для прототипов."""
    def clone(self):
        return copy.deepcopy(self)


class Rectangle(Prototype):
    def __init__(self, width, height):
        self.width = width
        self.height = height


    def __str__(self):
        return f"Rectangle({self.width}, {self.height})"


class Circle(Prototype):
    def __init__(self, radius):
        self.radius = radius


    def __str__(self):
        return f"Circle(radius={self.radius})"


class PrototypeManager:
    """Менеджер прототипов."""
    def __init__(self):
        self._prototypes = {}


    def register_prototype(self, name, prototype):
        self._prototypes[name] = prototype


    def unregister_prototype(self, name):
        if name in self._prototypes:
            del self._prototypes[name]


    def get_prototype(self, name):
        prototype = self._prototypes.get(name)
        if not prototype:
            raise ValueError(f"Прототип '{name}' не найден")
        return prototype.clone()


# Создание менеджера и регистрация прототипов
manager = PrototypeManager()
manager.register_prototype("small_rectangle", Rectangle(10, 5))
manager.register_prototype("big_circle", Circle(20))


# Использование менеджера
rect = manager.get_prototype("small_rectangle")
circle = manager.get_prototype("big_circle")


print(rect)   # Rectangle(10, 5)
print(circle) # Circle(radius=20)
