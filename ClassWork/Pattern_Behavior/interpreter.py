
from abc import ABC, abstractmethod


# Абстрактное выражение
class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass


# Терминальное выражение (число)
class Number(Expression):
    def __init__(self, value):
        self.value = value


    def interpret(self, context):
        return self.value


# Нетерминальное выражение (сложение)
class Add(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)


# Нетерминальное выражение (вычитание)
class Subtract(Expression):
    def __init__(self, left, right):
        self.left = left
        self.right = right


    def interpret(self, context):
        return self.left.interpret(context) - self.right.interpret(context)


# Клиентский код
# (5 + 3) - 2
expression = Subtract(
    Add(Number(5), Number(3)),
    Number(2)
)


# Интерпретация выражения
result = expression.interpret(None)
print(f"Result: {result}")  # Output: 6

