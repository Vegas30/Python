# # ^ циркумфлекс
# 1 Написать функцию, которая принимает два множества и возвращает их
# объединение, пересечение, разность, симметричную разность
def union_sets(set1, set2):
    # return set1.union(set2)
    return set1 | set2


def intersection_sets(set1, set2):
    return set1.intersection(set2)
    # return set1 & set2


def difference_sets(set1, set2):
    return set1 - set2
    # return set1.difference(set2)


def symmetric_diff_sets(set1, set2):
    return set1.symmetric_difference(set2)
    # return set1 ^ set2


set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(union_sets(set1, set2))
print(intersection_sets(set1, set2))
print(difference_sets(set1, set2))
print(symmetric_diff_sets(set1, set2))


# 2 Функцию, которая принимает два множества и проверяет, является ли
# первое множество подмножеством (надмножеством) второго
def is_subset(set1, set2):
    return set1.issubset(set2)
    # return set1 <= set2
    # return set1 < set2


def is_superset(set1, set2):
    return set1.issuperset(set2)
    # return set1 >= set2
    # return set1 > set2


def is_disjoint(set1, set2):
    return set1.isdisjoint(set2)


set1 = {1, 2}
set2 = {1, 2, 3}
print(is_subset(set1, set2))
print(is_superset(set1, set2))
print(is_disjoint(set1, set2))


# Функция, принимает список возвращает множество уникальных элементов
# этого списка
def set_elements(lst):
    return set(lst)


lst = [1, 2, 2, 3, 3, 4, 3, 5, 6, 5]
print(list(set_elements(lst)))

# 3. Функция, принимает список чисел и возвращает множество уникальных
# четных чисел
lst = [1, 2, 2, 3, 4, 4, 5, 6]
result = set(filter(lambda x: x % 2 == 0, lst))
print(result)

# 4. Используйте включение множеств для создания множества квадратов чисел
# от 1 до 10
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = set(map(lambda x: x ** 2, lst))

result = {x ** 2 for x in range(1, 10 + 1)}

# 5. Создайте множество чисел от 1 до 100, которые делятся на 5 или на 7
result = {x for x in range(1, 100 + 1) if x % 5 == 0 or x % 7 == 0}
result = set(filter(lambda x: x % 5 == 0 or x % 7 == 0, range(1, 100 + 1)))

# 6. Написать функцию, которая сортирует элементы множества
set1 = {1, 3, 4, 2}
result = sorted(set1)

# 7. Напишите функцию, которая принимает два множества чисел и
# возвращает множество, состоящее из элементов, которые присутствуют
# в обоих множествах и являются четными.
set1 = {1, 2, 3, 4, 6, 7}
set2 = {2, 4, 5, 6, 7}  # {2,4,6}
result = set(filter(lambda x: x % 2 == 0, set1.intersection(set2)))
result = {x for x in set1.intersection(set2) if x % 2 == 0}

# 8. Двумерный список и возвращает множество, которые уникальны для каждого
# списка ( не встречаются в других списках)
lists = [
    [1, 2, 3],
    [3, 4, 5],
    [5, 6, 7]
]  # {1,2,4,6,7}

numbers = sum(lists, [])
numbers = [num for sublist in lists for num in sublist]

print(set(numbers))
print(numbers)

result = {num for num in numbers if numbers.count(num) == 1}
print(result)

# 9. Напишите функцию, которая принимает множество чисел и возвращает
# подмножество, состоящее из простых чисел.
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

# 10. Дано множество чисел и два числа а и b. Подсчитайте кол-во элементов
# множества, которые находятся в диапазоне от a до b включительно.
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
a, b = 3, 7
result = len(set(x for x in set1 if a <= x <= b))
result = len({x for x in set1 if a <= x <= b})

# 11. Даны два списка чисел. Проверьте, пересекаются ли они, и если нет
# то верните их симметрическую разность. Если перескаются, верните
# пустой список.
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
intersect = list(set(lst1) ^ set(lst2)) if not set(lst1) & set(lst2) else []
# ------------------------------------------------------------------
intersect = set(lst1) & set(lst2)
if intersect:
    result = []
else:
    result = list(set(lst1) ^ set(lst2))
print(result)
# --------------------------------------------------------------------
for i in sorted(lst1):
    for j in sorted(lst2):
        if i == j:
            result = []
            break
else:
    result = list(set(lst1) ^ set(lst2))
print(result)
# ------------------------------------------------

# 12. Дан список чисел. Создайте два множества: одно с числами, которые
# делятся на 2, и другое с числами, которые делятся на 3. Найдите их
# объединение, пересечение и разность.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
set1 = {x for x in numbers if x % 2 == 0}
set2 = {x for x in numbers if x % 3 == 0}

union_set = set1 | set2
interesect_set = set1 & set2
difference_set = set1 - set2
print(union_set, interesect_set, difference_set)

# 13. Дан список чисел и целое число. Найдите все уникальные ПАРЫ
# чисел в списке, которые в сумме дают целое число. И отсортируйте.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10  # {(1,9), (2,8), ...}

pairs = set()
for i in set(numbers):
    for j in set(numbers):
        if i + j == target:
            pairs.add((i, j))
set_result = set(sorted(pairs))  # ? порядок элементов при переводе
print(set_result)

# 14. Дан список чисел. Удалите наибольшее и наименьшее значение, и
# верните оставшиеся уникальные элементы
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 4, 5, 3, 4, 7, 8, 9, 10, 10, 10, 10]
set_numbers = set(numbers[:])
set_numbers.remove(max(set_numbers))
set_numbers.discard(min(set_numbers))
print(set_numbers)

# 15. Дан список чисел и несколько пар чисел, каждая пара определяет
# диапазон. Подсчитайт количество элементов списка в каждом диапазоне.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ranges = [(1, 3), (4, 6), (7, 10)]
# [3,3,4]
counts = [len([num for num in numbers if r[0] <= num <= r[1]]) for r in ranges]
# -----------------------------------------
count = 0
for j in ranges:
    for i in numbers:
        if i >= j[0] and i <= j[1]:
            count += 1
# --------------------------------------------
result = [len(list(filter(lambda x: r[0] <= x <= r[1], numbers))) for r in ranges]
print(result)

# 16. Дан список чисел и целое число k. Найдите все уникальные пары
# чисел в списке, произведение которых кратно k.
numbers = [1, 2, 2, 3, 4, 5, 6]
k = 4

pairs = set()
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if (numbers[i] * numbers[j]) % k == 0:
            pairs.add((numbers[i], numbers[j]))
print(pairs)

# 17. Напишите программу, которя находит множество общих делителей
# двух чисел.
num1 = 28
num2 = 35
list1 = set()
# ----------------------------------------
for i in range(1, 35 + 1):
    if num1 % i == 0 and num2 % i == 0:
        list1.add(i)
print(list1)
# ---------------------------------------
set1 = {i for i in range(1, num1 + 1) if a % i == 0}
set2 = {i for i in range(1, num2 + 1) if b % i == 0}
result = set1.intersection(set2)
print(result)
# -----------------------------------------
set1 = {i for i in range(1, min(num1, num2) + 1) if num1 % i == 0 and num2 % i == 0}
print(set1)

# 18. Напишите программу, которая проверяет, имеют ли два множества
# хотя бы один общий элемент
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}
if not set1.isdisjoint(set2):
    print("Имеет")
else:
    print("Не имеет")

if set1 & set2:
    print("Имеет")
else:
    print("Не имеет")

# 19. Напишите программу, которая находит наибольший элемент в пересе-
# чении нескольких множеств
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
set3 = {4, 5, 6, 7}
result = max(set1 & set2 & set3)
print(result)

# 20. Программа, находит все возможные пары элементы из двух множеств
set1 = {1, 2, 3}
set2 = {4, 5}
result = {(i, j) for i in set1 for j in set2}

# 21. Напишите проограмму, которая находит все возможные комбинации
# элементов двух множеств, сумма которых меньше заданного числа k
set1 = {1, 2, 3}
set2 = {4, 5, 6}
k = 8
result = {(i, j) for i in set1 for j in set2 if i + j < k}

# 22. Программа, которая проверяет, перескаются ли три множества
set1 = {1, 2, 3, 4}
set2 = {1, 2, 3}
set3 = {3, 5, 6}
result = bool(set1 & set2 & set3)
print(result)
