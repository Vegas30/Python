# # ^ циркумфлекс
import random

#
# result = {1, 2, 3}
# for i in result:
#     print(i)
#
# my_set = ('abc')
# print(my_set)
#
# for i in my_set:
#     print(i)
#
#
# # Написать функцию которая принимает два множ и возвращ объединение,
#
# def union_sets(set1, set2):
#     return set1.union(set2)
#     # return set1 | set2
#
#
# def intersectio_sets(set1, set2):
#     return set1.intersection(set2)
#     # return set1 & set2
#
#
# # Функцию, которая принимает список чисел и возвращает множество уникальных четных чисел
#
# def func(list1):
#     res = set(filter(lambda x: x % 2 == 0, list1))
#     return res
#
#
# # Используйте включение множеств для создания множества квадратов чисел от 1 до 10
#
# result = {x ** 2 for x in range(1, 11)}

# Создайте множество чисел от 1 до 100, которые делятся на 5 или на 7
# result = {x for x in range(1, 100+1) if x % 5 == 0 or x % 7 == 0}
# result = set(filter(lambda x: x % 5 == 0 or x % 7 == 0, range(1, 100)))
# print(result)


# Написать функцию, которая принимает два множества чисел и возвращает множество,
# состоящее из элементов, которые присутствуют в обоих множествах и являются четными.

set1 = {1, 2, 3, 4, 6, 7}
set2 = {2, 4, 5, 6, 7}  # {2,4,6}
result = set(filter(lambda x: x % 2 == 0, set1.intersection(set2)))
print(result)
result = {x for x in set1.intersection(set2) if x % 2 == 0}
print(result)

# Написать функцию, которая принимает двумерный список и возвращает множество,
# которые уникальные для каждого списка (не встречаются в других списках)
lists = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]  # {1,2,4,6,7}

# numbers = sum(lists, [])
numbers = [num for sublist in lists for num in sublist]

result = {num for num in numbers if numbers.count(num) == 1}
print(result)

# Напишите функцию, которая принимает множество чисел и возвращает подмножество, состоящее из простых чисел.

set1 = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


result = {num for num in set1 if is_prime(num)}
print(result)
