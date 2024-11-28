from abc import ABC, abstractmethod


# Интерфейс компонента
class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass

    # Конкретный компонент


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "Базовый компонент"

    # Базовый декоратор


class Decorator(Component):
    def __init__(self, component: Component):
        self._component = component

    def operation(self) -> str:
        return self._component.operation()

    # Конкретный декоратор A


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"Декоратор A({super().operation()})"

    # Конкретный декоратор B


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"Декоратор B({super().operation()})"

    # Использование декораторов


component = ConcreteComponent()
decoratorA = ConcreteDecoratorA(component)
decoratorB = ConcreteDecoratorB(decoratorA)

print(decoratorB.operation())