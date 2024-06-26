# lambda - функция принимает три числа и возвращает максимум между суммой и разностью чисел
import random
from functools import reduce
#
# result = lambda x, y, z: max(x + y + z, x - y - z)
# print(result(3, 4, 5))
#
# # Написать программу которая преобразует список цифр в целые числа.
# numbers = [1, 2, 3, 4]
# result = list(map(lambda x: x + 10, numbers))
# result[0] = 10
# print(result)
#
# numbers = [1, 2, 3, 4]
# numbers_new = reduce(lambda x, y: str(x) + str(y), numbers)
#
# print(numbers_new)
#
# result = reduce(lambda x, y: x * 10 + y, numbers)
#
# numbers = [[1, 2], [3, 4], [4, 5]]
# result = reduce(lambda x, y: x + y, numbers)
# result = reduce(lambda x, y: x.extend(y) or x, numbers, [])
# print(result)
#
# numbers = [0, 2, 3, 4, 5]
# result = reduce(lambda x, _: x + 1, numbers, 0)
# print(result)
#
# # Факториал числа 5. 5! = 1*2*3*4*5 = ?
#
# result = reduce(lambda x, y: x * y, range(1, 5 + 1))
# print(result)
#
# array = [random.randint(-10, 10) for _ in range(5)]
# print(array)
#
# numbers = [1, 2, 3, 4]
# result = sum(map(lambda x: x ** 2, numbers)
#              )
# result = reduce(lambda x, y: x + y ** 2, numbers)
# print(result)
#
# # Принимает список чисел, затем фильтрует только четные числа, затем удваивает
# numbers = [1, 2, 3, 4, 5, 6]
# result = list(filter(lambda x: x % 2 == 0, numbers))
# result1 = list(map(lambda x: x * 2, result))
# print(result1)
#
# #
# numbers = [123, 1234, 4567, 12]
# result = list(filter(lambda x: len(str(abs(x))) > 3, numbers))
# reverse = list(map(lambda x: str(abs(x))[::-1]), result)
# print(result)

result = list(map((lambda x: x ** 2), (filter(lambda x: x < 0, (x for x in range(-10, 10+1))))))

print(result)
