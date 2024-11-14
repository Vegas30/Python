import json


class Person:

    def update(self, json_str):
        self.__dict__ = json.loads(json_str)


json_str = '{"name": "Bob", "age": 25}'

person1 = Person()
person1.update(json_str)
print(person1.__dict__)
person1.age = 30
print(person1.__dict__)
person1.ages = 130
print(person1.__dict__)
