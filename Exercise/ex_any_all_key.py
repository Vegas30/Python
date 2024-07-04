# 1. Даны два списка чисел. Проверьте, что никакой элемент из
# первого списка не содержится во втором списке.
from functools import reduce

list1 = [10, 11, 12]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = all(elem not in list2 for elem in list1)

# 2. Даны два списка чисел. Проверьте, что хотя бы один
# элемент из первого списка содержится во втором списке.
list1 = [3, 10, 15]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = any(elem in list2 for elem in list1)

# 3. Даны два списка чисел. Проверьте, что все элементы
# первого списка, которые больше 5, содержатся во втором
# списке.
list1 = [3, 6, 7, 9]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = all(elem in list2 for elem in list1 if elem > 5)

# 4. Даны два списка чисел. Проверьте, что все элементы
# второго списка являются квадратами чисел из первого
# списка.
list1 = [1, 2, 3]
list2 = [1, 4, 9]
result = all(elem ** 2 in list2 for elem in list1)

# 5. Даны два списка чисел. Проверьте, что сумма всех чисел
# первого списка содержится во втором списке.
list1 = [1, 2, 3]
list2 = [6, 7, 8, 9]

result = sum(list1) in list2

# 6. Даны два списка чисел. Проверьте, что произведение всех
# чисел второго списка содержится в первом списке.
list1 = [1, 2, 3, 6, 24]
list2 = [2, 3, 4]

pr = 1
for elem in list2:
    pr *= elem
    result = pr in list1

pr = reduce(lambda x, y: x * y, list2)
result = pr in list1

# 7. Даны два списка чисел. Проверьте, что все простые числа из
# первого списка содержатся во втором списке.
list1 = [2, 3, 4, 5, 6]
list2 = [1, 2, 3, 5, 7, 11]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


prime = [elem for elem in list1 if is_prime(elem)]
result = all(elem in list2 for elem in prime)

# 8. Даны два списка чисел. Проверьте, что хотя бы одно четное
# число из первого списка содержится во втором списке.
list1 = [1, 3, 5, 8]
list2 = [6, 7, 8, 9, 10]

result = any(x in list2 for x in list1 if x % 2 == 0)

# 9. Даны два списка чисел. Проверьте, что сумма всех чисел,
# содержащихся в обоих списках, присутствует в первом
# списке.
list1 = [15, 30, 45, 60]
list2 = [5, 10, 15]

result = sum(list1 + list2) in list1

# 10. Даны два списка чисел. Проверьте, что любой элемент из
# второго списка делится без остатка на любой элемент из
# первого списка.
list1 = [1, 2, 3]
list2 = [6, 12, 18]

result = None
for elem in list2:
    for elem2 in list1:
        if not elem % elem2 == 0:
            result = False
    result = True
print(result)

result = all((any(b % a == 0 for a in list1) for b in list2))

print(result)

# 11. Даны два списка чисел. Проверьте, что все элементы
# первого списка являются чётными и содержатся во втором
# списке.
list1 = [2, 4, 6, 8]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result1 = all(x % 2 == 0 for x in list1)
if result1:
    result = all(x in list2 for x in list1 if x % 2 == 0)
else:
    print("Не все элементы четные")
# ----
result1 = all(x % 2 == 0 and x in list2 for x in list1)

print(result1)

# Задачи на key:
# 1. Дан список чисел. Найдите максимальный элемент по
# модулю.
numbers = [-10, 20, -30, 40, -50]

result = max(numbers, key=abs)
print(result)

# 2. Дан список чисел. Найдите минимальный элемент по
# модулю.
numbers = [-10, 20, -30, 40, -50]

result = min(numbers, key=abs)
print(result)

# 3. Дан список чисел. Отсортируйте его по возрастанию
# квадратов чисел.
numbers = [1, -8, 3, -4, 5]

result = sorted(numbers, key=lambda x: x ** 2)
print(result)

# 4. Дан список чисел. Отсортируйте его по возрастанию
# последней цифры чисел.
numbers = [15, 22, 37, 41, 56]

result = sorted(numbers, key=lambda x: x % 10)

# 5. Дан список чисел. Найдите элемент с наибольшей суммой
# цифр.
numbers = [123, 456, 789, 234, 567]
result = max(numbers, key=lambda x: sum(int(digit) for digit in str(x)))
print(result)

# 6. Дан список чисел. Найдите элемент с наименьшей суммой
# цифр.
numbers = [123, 456, 789, 234, 567]
result = min(numbers, key=lambda x: sum(int(digit) for digit in str(x)))
print(result)

# 7. Дан список чисел. Отсортируйте его по возрастанию
# количества делителей.
numbers = [12, 6, 15, 10, 8]


def num_dividers(n):
    # count = 0
    # for i in range(1, n + 1):
    #     if n % 1 == 0:
    #         count += 1
    # return count
    # -----
    return sum(1 for i in range(1, n + 1) if n % i == 0)


result = sorted(numbers, key=num_dividers)

# 9. Дан список чисел. Найдите минимальный элемент по
# количеству делителей.
numbers = [12, 6, 15, 10, 8]

result = sorted(numbers, key=lambda x: x % 7)