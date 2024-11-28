from abc import ABC, abstractmethod


# Компонент: общий интерфейс
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

    # Листовой элемент: конкретный объект


class Leaf(Component):
    def operation(self) -> str:
        return "Листовой элемент"

    # Композиция: объект, который может содержать другие компоненты


class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component: Component) -> None:
        self.children.append(component)

    def operation(self) -> str:
        result = "Композиция:\n"
        for child in self.children:
            result += f"  {child.operation()}\n"
        return result

    # Использование паттерна Composite


leaf1 = Leaf()
leaf2 = Leaf()
composite1 = Composite()
composite2 = Composite()

composite1.add(leaf1)
composite1.add(leaf2)

composite2.add(leaf1)
composite1.add(composite2)
print(composite1.operation())