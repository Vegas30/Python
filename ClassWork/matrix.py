# 12.1. Дан двумерный массив.
# а) Вывести на экран элемент, расположенный в правом верхнем
# углу массива.
# б) Вывести на экран элемент, расположенный в левом нижнем
# углу массива.

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# list2 = [1, 2, 3, 4]
# result = list2[1]
#
# result_matrix = matrix[0][2]
#
# print(result_matrix)
#
# result = matrix[2][0]
# print(result)

import random

# количество строк в двумерном списке row
row = random.randint(1, 10)
print(row)
# количество столбцов в двумерном списке column
column = random.randint(3, 7)
print(column)
matrix = [[random.randint(-10, 10) for _ in range(column)] for _ in range(row)]
print(matrix)

for row in matrix:
    for num in row:
        print(num, end="\t")
    print()

for row in matrix:
    print(row)
