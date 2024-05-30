# 6.45. Даны числа a1,a2,...,a10. Определить их среднее
# арифметическое.

import random


def calculate_func():
    sum = 0

    for i in range(1, 11):
        a = random.randint(0, 10)
        print(f"a{i} = {a}", end="  ")
        sum += a
        result = sum / 10

    return result


def main():
    sum_result = calculate_func()
    print(f"\nCреднее арифметическое чисел равно {sum_result:.2f}")


main()
