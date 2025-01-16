from collections import deque


def bfs_with_queue(node):
    queue = deque([node])  # Очередь, где начинаем с корня дерева
    while queue:
        current_node = queue.popleft()  # Извлекаем узел из очереди
        print(current_node.value, end=" ")  # Обрабатываем текущий узел
        queue.extend(current_node.children)  # Добавляем детей в прямом порядке

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


class Tree:
    def __init__(self):
        self.root = None


    def add_node(self, parent_value, value):
        if not self.root:
            self.root = TreeNode(value)  # Создаём корень, если его ещё нет
            return
        parent = self.find_node(self.root, parent_value)
        if parent:
            parent.children.append(TreeNode(value))
        else:
            print(f"Родительский узел {parent_value} не найден.")


    def find_node(self, node, value):
        if not node:
            return None
        if node.value == value:
            return node
        for child in node.children:
            found = self.find_node(child, value)
            if found:
                return found
        return None


    def traverse(self, node):
        if not node:
            return
        print(node.value, end=" ")
        for child in node.children:
            self.traverse(child)


# Создаём дерево
tree = Tree()
tree.add_node(None, "A")  # Добавляем корень
tree.add_node("A", "B")
tree.add_node("A", "C")
tree.add_node("B", "D")
tree.add_node("B", "E")
tree.add_node("C", "F")
tree.add_node("C", "G")


# Обходим дерево
tree.traverse(tree.root)
# Вывод: A B D E C F G

