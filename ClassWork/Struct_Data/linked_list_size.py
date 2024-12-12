import sys


class Node:
    def __init__(self, data):
        self.data = data  # Данные
        self.next = None  # Ссылка на следующий узел


class LinkedList:
    def __init__(self):
        self.head = None  # Начало списка

    def append(self, data):
        new_node = Node(data)
        if not self.head:  # Если список пуст
            self.head = new_node
        else:  # Найти конец списка и добавить узел
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


linked_list = LinkedList()
for i in range(10):
    linked_list.append(i)
    # Память текущего списка и всех его узлов
    current = linked_list.head
    total_size = sys.getsizeof(linked_list)  # Память на сам объект списка
    while current:
        total_size += sys.getsizeof(current)  # Память на объект узла
        total_size += sys.getsizeof(current.data)  # Память на данные узла
        current = current.next
        print(f"Elements: {i + 1}, size in bytes: {total_size}")
    print(f"Elements: {i + 1}, Total size in bytes: {total_size}")
