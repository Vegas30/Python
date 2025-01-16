from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs_with_queue(node):
    queue = deque([node])  # Очередь, где начинаем с корня дерева
    while queue:
        current_node = queue.popleft()  # Извлекаем узел из очереди
        print(current_node.value, end=" ")  # Обрабатываем текущий узел
        queue.extend(current_node.children)  # Добавляем детей в прямом порядке




def dfs_with_stack(node):
    stack = [node]  # Стек, где начинаем с корня дерева
    while stack:
        current_node = stack.pop()  # Извлекаем узел из стека
        print(current_node.value, end=" ")  # Обрабатываем текущий узел
        stack.extend(reversed(current_node.children))  # Добавляем детей в обратном порядке


# Создание дерева
root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
root.children.append(child1)
root.children.append(child2)

child1.children.append(TreeNode("D"))
child1.children.append(TreeNode("E"))
child2.children.append(TreeNode("F"))
child2.children.append(TreeNode("G"))

# Тестирование обходов
print("DFS (обход в глубину):")
dfs_with_stack(root)  # Вывод: A B D E C F G

print("\nBFS (обход в ширину):")
bfs_with_queue(root)  # Вывод: A B C D E F G



