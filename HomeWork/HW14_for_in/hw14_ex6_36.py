# 6.36. Даны натуральное число n и вещественные числа a1,a2, .., an.
# Определить сумму всех вещественных чисел.

import random


def calculate_func(n):
    sum = 0

    for i in range(1, n + 1):
        a = random.uniform(0, 1)
        print(f"a{i} = {round(a, 2)}", end=" ")
        sum += a

    return sum


def main():
    n = random.randint(1, 10)
    sum_result = calculate_func(n)
    print(f"\nСумма всех вещественных чисел при n = {n} равна {sum_result:.2f}")


main()
