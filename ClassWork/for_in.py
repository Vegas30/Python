import random
# 6.1. Напечатать ряд чисел 20 в виде: 20 20 20 20 20 20 20 20 20 20.

print("№ 6.1.")

amount = random.randint(0, 50)

for _ in range(amount):
    print(20, end = " ")

# 6.2. Составить программу вывода любого числа любое заданное
# число раз в виде, аналогичном показанному в предыдущей задаче.

print("\n№ 6.2.")

i = float(input("Введите любое число: "))
amount = int(input("Введите количество повторений введённого числа: "))

for _ in range(amount):
    print(i, end = " ")


# 6.7. Напечатать таблицу соответствия между весом в фунтах и весом
# в килограммах для значений 1, 2, ..., 10 фунтов (1 фунт = 453 г)

print("\n№ 6.7.")

print("Фунты  Килограммы")
for i in range(1, 10+1):
    print(f" {i} \t\t {round(i * 0.453, 3)}")


# 6.20. Найти:
# а) среднее арифметическое всех целых чисел от 1 до 1000;
# б) среднее арифметическое всех целых чисел от 100 до b (значение b
# вводится с клавиатуры; b >= 100);
# в) среднее арифметическое всех целых чисел от a до 200 (значения a
# и b вводятся с клавиатуры; a <= 200);
# г) среднее арифметическое всех целых чисел от a до b (значения a и b
# вводятся с клавиатуры; b >= a).

print("\n№ 6.20.")

a = int(input("Введите целое число (a <= 200): "))
b = int(input("Введите целое число (b >= 100): "))

sum_numbers = 0
count = 0

for i in range(1, 1000 + 1):
    sum_numbers += i
    count += 1
average_numbers = sum_numbers / count
print(f"Среднее арифметическое всех целых чисел от 1 до 1000 равно {average_numbers}")

sum_numbers = 0
count = 0
if not(b >= 100):
    print("При таких значении переменной условие задачи неверно")
else:
    for i in range(100, b + 1):
        sum_numbers += i
        count += 1
    average_numbers = sum_numbers / count
    print(f"Среднее арифметическое всех целых чисел от 100 до {b} равно {average_numbers}")

sum_numbers = 0
count = 0
if not(a <= 200):
    print("При таких значении переменной условие задачи неверно")
else:
    for i in range(a, 200 + 1):
        sum_numbers += i
        count += 1
    average_numbers = sum_numbers / count
    print(f"Среднее арифметическое всех целых чисел от {a} до 200 равно {average_numbers}")

sum_numbers = 0
count = 0
if not(b >= a):
    print("При таких значении переменной условие задачи неверно")
else:
    for i in range(a, b + 1):
        sum_numbers += i
        count += 1
    average_numbers = sum_numbers / count
    print(f"Среднее арифметическое всех целых чисел от {a} до {b} равна {average_numbers}")