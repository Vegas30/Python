from binarytree import Node

# Создаем корневой узел дерева
root = Node(1)

# Создаем дочерние узлы
root.left = Node(2)
root.right = Node(3)
# Создаем еще несколько узлов для левого поддерева
root.left.left = Node(4)
root.left.right = Node(5)

# Создаем еще несколько узлов для правого поддерева
root.right.left = Node(6)
root.right.right = Node(7)

# Теперь у нас есть бинарное дерево:
#         1 
#       /   \
#      2     3
#     / \   / \
#    4   5 6   7


# Доступ к значениям узлов
print(root.value)  # Выведет 1 (значение корня)
print(root.left.value)  # Выведет 2 (значение левого потомка)
print(root.right.value)  # Выведет 3 (значение правого потомка)

# Можно также проверять, есть ли у узла потомки
print(root.left.left)  # Выведет: Node(4)
print(root.right.right)  # Выведет: Node(7)
print(root.left.left.left)  # Выведет: None, так как у этого узла нет левого потомка