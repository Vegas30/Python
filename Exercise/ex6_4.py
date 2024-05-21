# 6.4. Дана последовательность из n вещественных чисел,
# начинающаяся с отрицательного числа. Определить, какое количество
# отрицательных чисел записано в начале последовательности.
# Условный оператор не использовать.

def calculate_func():
    summ = 0
    count = 0
    number = float(input("Введите число: "))
    while number < 0:
        summ += number
        count += 1
        number = float(input("Введите число: "))
    return summ


def main():
    result = calculate_func()
    print(result)

main()
