# 12.36. Дан двумерный массив. Определить:
# а) сумму всех элементов второго столбца массива;
# б) сумму всех элементов k-й строки массива.

import random
import numpy as np

row = random.randint(1, 3)
print(row)
# количество столбцов в двумерном списке column
column = random.randint(3, 3)
print(column)

matrix = [[random.randint(-10, 10) for _ in range(column)] for _ in range(row)]
for roww in matrix:
    print(roww)

print("-----------------------")

matrix_res = [[matrix[i][j] for i in range(row)] for j in range(1,-2)]

result = np.sum(matrix_res)

print(result)