# 12.34. Дан двумерный массив. Вывести на экран его элементы
# следующим образом:
# а) сначала элементы первой строки справа налево, затем второй
# строки справа налево и т. п.;

import random

row = random.randint(1, 3)
print(row)
# количество столбцов в двумерном списке column
column = random.randint(3, 3)
print(column)

matrix = [[random.randint(-10, 10) for _ in range(column)] for _ in range(row)]
for roww in matrix:
    print(roww)

print("-----------------------")

# for i in range(row):
#     for j in range(column-1, -1, -1):
#         print(matrix[i][j])
#     print()
#
# for rows in matrix:
#     rows.reverse()
#
# print("-----------------------")
#
# for r in matrix:
#     print(r)
#
#
# # в) сначала элементы первого столбца сверху вниз, затем второго
# # столбца сверху вниз и т. п.;
#
#
# matrix2 =[[matrix[i][j] for i in range(row)] for j in range(column)]
# print(matrix2)

# г) сначала элементы первого столбца снизу вверх, затем второго
# столбца снизу вверх и т. п.

matrix3 = [[matrix[i][j] for i in range(row-1, -1, -1)] for j in range(column)]
print(matrix3)