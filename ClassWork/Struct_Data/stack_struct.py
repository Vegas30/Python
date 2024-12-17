class Stack:
    def __init__(self):
        self.stack = []


    def push(self, item):
        """Добавляет элемент в стек."""
        self.stack.append(item)


    def pop(self):
        """Удаляет верхний элемент и возвращает его."""
        if self.is_empty():
            raise IndexError("Попытка извлечь элемент из пустого стека")
        return self.stack.pop()


    def peek(self):
        """Возвращает верхний элемент без его удаления."""
        if self.is_empty():
            raise IndexError("Стек пуст")
        return self.stack[-1]


    def is_empty(self):
        """Проверяет, пуст ли стек."""
        return len(self.stack) == 0


    def size(self):
        """Возвращает размер стека."""
        return len(self.stack)
