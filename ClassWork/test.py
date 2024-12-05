class Parent:
    __slots__ = ('attr1',)

class Child(Parent):
    __slots__ = ('attr2',)

obj = Child()
obj.attr1 = "attr1"
obj.attr2 = "attr2"

print(obj.__slots__)
print(obj.attr1)