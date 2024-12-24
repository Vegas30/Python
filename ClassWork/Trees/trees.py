from anytree import Node, RenderTree, findall, find
from anytree.exporter import JsonExporter, DictExporter
from binarytree import build, heap, bst


# Создаём узлы
root = Node("Root")  # Корень дерева
child1 = Node("Child1", parent=root)  # Потомок Root
child2 = Node("Child2", parent=root)
grandchild1 = Node("GrandChild1", parent=child1)
# Доступ к отрибутам
print(root.is_root)
# True
print(child1.is_leaf)
# False
print(grandchild1.is_leaf)
# True

child1.parent = child2
print(child2.children)
print(root.descendants)

for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")

root = Node("Root")  # Корень дерева
child1 = Node("Child1", parent=root)  # Потомок Root
child2 = Node("Child2", parent=root)
grandchild1 = Node("GrandChild1", parent=child1)

for pre, fill, node in RenderTree(root, childiter=lambda children: reversed(children)):
    print(f"{pre}{node.name}")

root = Node("Root")  # Корень дерева
child1 = Node("Child1", parent=root)  # Потомок Root
child2 = Node("Child2", parent=root)
grandchild1 = Node("GrandChild1", parent=child1)

for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name}")

root = Node("Root", size=100)  # Корень дерева
child1 = Node("Child1", parent=root, size=50)  # Потомок Root
child2 = Node("Child2", parent=root, size=30)
grandchild1 = Node("GrandChild1", parent=child1)

for pre, fill, node in RenderTree(root):
    print(f"{pre}{node.name} (size={getattr(node, 'size', 'N/A')})")

root = Node("Root")  # Корень дерева
child1 = Node("Child1", parent=root, size=10)  # Потомок Root
child2 = Node("Child2", parent=root, size=20)
grandchild1 = Node("GrandChild1", parent=child1, size=5)

nodes = findall(root, lambda n: getattr(n, 'size', 0) > 5)
print([node.name for node in nodes])

nodes = findall(root, lambda n: n.name.startswith("C"))
print([node.name for node in nodes])

root = Node("Root")  # Корень дерева
child1 = Node("Child1", parent=root, size=15)  # Потомок Root
child2 = Node("Child2", parent=root, size=25)
grandchild1 = Node("GrandChild1", parent=child1, size=5)

exporter = JsonExporter(indent=2, sort_keys=True)
json_data = exporter.export(root)
print(json_data)

root = Node("Root")  # Корень дерева
child1 = Node("Child1", parent=root, size=15)  # Потомок Root
child2 = Node("Child2", parent=root, size=25)
grandchild1 = Node("GrandChild1", parent=child1, size=5)
exporter = DictExporter()
dict_data = exporter.export(root)
print(dict_data)

tree = build([1,2,3,4,5, None, 7])
print(tree)

tree = heap(height=3, is_max=True)
print(tree)
tree = bst(height=3, is_perfect=False)
print(tree)
