# 4.25. Определить, верно ли, что при делении неотрицательного целого
# числа a на положительное число b получается остаток, равный
# одному из двух заданных чисел c или d.

a = int(input("Введите положительное целое число a "))
b = int(input("Введите положительное целое число b "))
c = float(input("Введите число c "))
d = float(input("Введите число d "))
if a <= 0 or b <= 0:
    print("Ошибка. Число должно быть положительным")
else:
    if (a / b == c) or (a / b == d):
        print("Верно")
    else:
        print("Не верно")