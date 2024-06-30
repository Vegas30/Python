# Использовать включение списка
# 1) Создать список квадратов от 1 до 10 включительно
import math

squares = [x ** 2 for x in range(10 + 1)]
print(squares)

even_num = [x for x in range(20 + 1) if x % 2 == 0]
print(even_num)

# Дан список чисел. Создать список, содержащиий сумму цифр каждого числа.

number = [123, 456, 789]
digit_sums = [sum(map(int, str(i))) for i in number]
print(digit_sums)

# Создать список из чисел от 1 до 20 включительно, стоящих на четных индексах (0,2,4,8,16,

even_list = [x for x in range(1, 20 + 1)][::2]
print(even_list)

# Создать список отрицательных чисел от 1 до 10 включительно.

negativ_numbers = [-x for x in range(1, 10)]
print(negativ_numbers)

# Создать список кортежей, каждый состоит из числа от 1 до 10 включительно и его квадрата

array_cortege = [(x, x ** 2) for x in range(1, 10)]
array_cortege2 = ([x, x ** 2] for x in range(1, 10))
print(array_cortege)
print(array_cortege2)

# Создать список кортежей, где каждый кортеж состоит из числа от 1 до 10 включительно и его факториала

list_cortege_num_factorial = [(x, math.factorial(x)) for x in range(1, 10 + 1)]
print(list_cortege_num_factorial)

# Создайте список чисел от 1 до 10 включительно, возведенных в степень их индекса в списке

list_index_enum = [x ** i for i, x in enumerate(range(1, 10 + 1))]
print(list_index_enum)

# Создайте список кортежей всех пар чисел от 1 до 10 включительно, которые в сумме дают четное число.

list_cortege_sum_even = [(x, y) for x in range(1, 10 + 1) for y in range(1, 10 + 1) if (x + y) % 2 == 0]

# Создайте список квадратов чисел от 1 до 20 включительно, если число четное, иначе оставьте без изменений.

result = [x ** 2 if x % 2 == 0 else x for x in range(1, 20 + 1)]
print(result)

# Сгенерируйте первые 10 чисел Фибонначи

fib = [0, 1]
[fib.append(fib[-1] + fib[-2]) for _ in range(8)]
print(fib)

# Создайте список всех троек чисел от 1 до 10 включительно, сумма которых равна 15.

list_sum_15 = [(x,y,z) for x in range(1, 10+1) for y in range(1, 10 +1) for z in range(1, 10 + 1) if x+y+z == 15]
print(list_sum_15)

