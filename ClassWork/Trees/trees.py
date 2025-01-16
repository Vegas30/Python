class Node:
    def __init__(self, key):
        self.key = key
        self.color = "RED"  # По умолчанию новый узел красный
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)  # Это фиктивный NIL-узел, черный
        self.TNULL.color = "BLACK"
        self.root = self.TNULL

        # Вставка нового узла

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.key = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = "RED"

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = "BLACK"
            return

        if node.parent.parent is None:
            return

        self.fix_insert(node)

        # Вспомогательная функция для корректировки дерева после вставки

    def fix_insert(self, k):
        while k.parent.color == "RED":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "RED":
                    u.color = "BLACK"
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "BLACK"
                    k.parent.parent.color = "RED"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "BLACK"

        # Левый поворот

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

        # Правый поворот

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

        # Поиск узла по ключу

    def search_tree(self, node, key):
        if node == self.TNULL or key == node.key:
            return node

        if key < node.key:
            return self.search_tree(node.left, key)
        return self.search_tree(node.right, key)

        # Вывод дерева в инфиксном порядке

    def inorder(self, node):
        if node != self.TNULL:
            self.inorder(node.left)
            print(f"{node.key} ({node.color})", end=" ")
            self.inorder(node.right)

        # Пример использования:


rbt = RedBlackTree()

# Вставляем элементы
rbt.insert(10)
rbt.insert(20)
rbt.insert(30)
rbt.insert(15)
rbt.insert(25)

# Выводим дерево в инфиксном порядке
rbt.inorder(rbt.root)