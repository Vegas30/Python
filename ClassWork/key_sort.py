# Отсортировать список списков по длине каждого внутреннего списка
from ClassWork.for_in import count

lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
lists.sort(key=len)
print(lists)

# Отсортировать список списков по сумме елементов каждого внутреннего списка
lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
lists.sort(key=sum)

# по последнему элементу каждого внутреннего списка
lists = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
lists.sort(key=lambda x: x[-1])
print(lists)

# Отсортировать список списков по четности первого элемента
lists = [[2, 2], [5, 4], [6, 7, 8, 9]]
lists.sort(key=lambda x: x[0] % 2)

# Отсортировать список списков по количеству четных чисел во внутреннем списке
lists = [[1, 2, 3], [2, 4, 6], [3, 5]]
lists.sort(key=lambda x: sum(1 for i in x if i % 2 == 0))

# Отсрортировать по сумме квадратов элементов каждого внутреннего списка
lists = [[1, 2, 3], [2, 4, 6], [3, 5]]
lists.sort(key=lambda x: sum(i ** 2 for i in x), reverse=True)

# Проверить наличие хотя бы одного положительного числа в списке
lists = [-5, -6, -6, 1, 2]
result = lambda x: any(i > 0 for i in x)
print(result(lists))

# Проверить что все элементы списка являются четными
lists = [-5, -6, -6, 1, 2]
result = lambda x: all(i % 2 == 0 for i in x)
print(result(lists))

# Отсортировать по количеству элементов равных 0
lists = [[0, 2, 3], [4, 0, 0], [6, 7, 8, 9]]
result = lists.sort(key=lambda x: x.count(0))
print(result)


