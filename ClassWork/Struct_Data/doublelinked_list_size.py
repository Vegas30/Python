import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def calculate_memory_usage(self):
        total_size = sys.getsizeof(self)  # Память на сам список
        total_size += sys.getsizeof(self.head)  # Память на ссылку head
        print(f"Память в bytes head {total_size}")
        total_size += sys.getsizeof(self.tail)  # Память на ссылку tail
        print(f"Память в bytes tail {total_size}")

        current = self.head
        while current:
            total_size += sys.getsizeof(current)  # Память на объект узла
            print(f"Память в bytes overhead {total_size}")
            total_size += sys.getsizeof(current.data)  # Память на данные узла
            print(f"Память в bytes data {total_size}")
            current = current.next
            print("------------")
        return total_size


dll = DoublyLinkedList()
for i in range(10):
    dll.append(i)
print(f"Total memory used by the doubly linked list: {dll.calculate_memory_usage()} bytes")
