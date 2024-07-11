# 12.7. Составить программу:
# а) заменяющую значение любого элемента пятой строки
# двумерного массива числом 1949;
# б) заменяющую значение всех элементов b двумерного массива числом a.
# С последующим выводом количества замененных элементов
import random

row = random.randint(1, 3)
print(row)
# количество столбцов в двумерном списке column
column = random.randint(3, 3)
print(column)

matrix = [[random.randint(-10, 10) for _ in range(column)] for _ in range(row)]
for roww in matrix:
    print(roww)

a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))

count = 0
for i in range(row):
    for j in range(column):
        print(matrix[i][j])
        if matrix[i][j] == b:
            matrix[i][j] = a
            count += 1

for rows in matrix:
    print(rows)

print(count)
