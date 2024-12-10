class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def add_to_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def add_to_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node


    def remove_front(self):
        if not self.head:
            print("Список пуст!")
            return
        self.head = self.head.next


    def find(self, value):
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False


    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")
