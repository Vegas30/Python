# Задача: Оптимизация отображения деревьев в лесу с использованием паттерна Flyweight
# Вы разрабатываете приложение для симуляции леса. В лесу может быть множество деревьев разных типов.
# Каждое дерево имеет следующие свойства:
#
# Уникальные свойства (конкретное дерево):
#
# Позиция на карте (x, y).
# Общие свойства (тип дерева):
#
# Название вида дерева (например, "Береза", "Дуб").
# Цвет листьев.
# Высота дерева.
# Условия задачи:
# Создайте структуру для хранения общих данных о деревьях, чтобы избежать дублирования (используйте Flyweight).
# Реализуйте класс для конкретного дерева, который будет ссылаться на общий объект типа дерева.
# Напишите фабрику, которая будет создавать и возвращать общие объекты типа дерева.
# Напишите код, который создает множество деревьев разных типов на карте, но при этом эффективно использует память.
# Пример:
# На вход подаются данные о деревьях в формате:
# [
#     {"type": "Береза", "color": "Зеленый", "height": 15, "x": 10, "y": 20},
#     {"type": "Береза", "color": "Зеленый", "height": 15, "x": 15, "y": 25},
#     {"type": "Дуб", "color": "Темно-зеленый", "height": 20, "x": 30, "y": 35},
# ]
# На выходе вы получите информацию о созданных объектах, включая общие свойства дерева, и сможете проверить,
# что для одного типа дерева используется один общий объект.
class BaseTree:
    """Летучий объект, который хранит общее состояние."""

    def __init__(self, name, color, height):
        self.name = name
        self.color = color
        self.height = height
        # Внутреннее состояние

    def operation(self):
        """Использует внешнее состояние."""
        print(f"{self.name} {self.color} {self.height}")

class TreeUnik:
    def __init__(self, x, y, tree_type: BaseTree):
        self.x = x
        self.y = y
        self.tree_type = tree_type

    def display(self):
        return f"Дерево типа {self.tree_type.name} на позиции ({self.x}, {self.y})"
class BaseTreeFactory:
    """Фабрика для управления летучими объектами."""

    def __init__(self):
        self._tree_types = {}
        self._trees = []
    def get_trees(self, name, color, height):
        """Возвращает существующий объект или создаёт новый."""
        key = (name, color, height)
        if key not in self._tree_types:
            self._tree_types[key] = BaseTree(name, color, height)
        return self._tree_types[key]

a = [
    {"type": "Береза", "color": "Зеленый", "height": 15},
    {"type": "Береза", "color": "Зеленый", "height": 15},
    {"type": "Дуб", "color": "Темно-зеленый", "height": 20},
]
factory = BaseTreeFactory()
# Создаём несколько летучих объектов с общим состоянием
flyweight1 = factory.get_trees(a[0]["type"], a[0]["color"], a[0]["height"])
flyweight2 = factory.get_trees(a[1]["type"], a[1]["color"], a[1]["height"])

# Применяем уникальное состояние
flyweight1.operation()
flyweight2.operation()

tree = TreeUnik(10,15, flyweight1)
print(tree.display())