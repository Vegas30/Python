# 4.45. Даны четыре целых числа. Определить сумму тех из них,
# которые кратны трем. Оператор цикла не использовать.

num_1 = int(input("Введите первое целое число: "))
num_2 = int(input("Введите второе целое число: "))
num_3 = int(input("Введите третье целое число: "))
num_4 = int(input("Введите четвертое целое число: "))

sum_digits = 0

if num_1 % 3 == 0:
    sum_digits += num_1
if num_2 % 3 == 0:
    sum_digits += num_2
if num_3 % 3 == 0:
    sum_digits += num_3
if num_4 % 3 == 0:
    sum_digits += num_4

print(f"Сумма чисел которые кратны трем: {sum_digits}")

