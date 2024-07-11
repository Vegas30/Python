# Посчитать сумму элементов главной и побочной диагонали

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [4, 5, 6]
]
summ = 0
for i in range(3):
    for j in range(3):
        if i == j:
            summ += matrix[i][j]

for i in range(3):
    summ += matrix[i][3-i-1]

print(summ)

# matrix[i][row-i-1]