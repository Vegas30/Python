class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Указатель на первый узел
        self.tail = None  # Указатель на последний узел


    def add_to_front(self, data):
        """Добавить элемент в начало списка"""
        new_node = Node(data)
        if not self.head:  # Если список пуст
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node


    def add_to_end(self, data):
        """Добавить элемент в конец списка"""
        new_node = Node(data)
        if not self.tail:  # Если список пуст
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node


    def delete_from_front(self):
        """Удалить элемент из начала списка"""
        if not self.head:  # Если список пуст
            return None
        data = self.head.data
        if self.head == self.tail:  # Если в списке только один элемент
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data


    def delete_from_end(self):
        """Удалить элемент из конца списка"""
        if not self.tail:  # Если список пуст
            return None
        data = self.tail.data
        if self.head == self.tail:  # Если в списке только один элемент
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return data


    def display_forward(self):
        """Вывести элементы списка от начала к концу"""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


    def display_backward(self):
        """Вывести элементы списка от конца к началу"""
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")


dll = DoublyLinkedList()


# Добавляем элементы
dll.add_to_front(10)
dll.add_to_front(20)
dll.add_to_end(5)


# Отображаем список
print("Прямой обход:")
dll.display_forward()  # 20 <-> 10 <-> 5 <-> None


print("Обратный обход:")
dll.display_backward()  # 5 <-> 10 <-> 20 <-> None


# Удаляем элементы
dll.delete_from_front()  # Удаляет 20
dll.delete_from_end()    # Удаляет 5


# Снова отображаем
print("После удаления:")
dll.display_forward()  # 10 <-> None
