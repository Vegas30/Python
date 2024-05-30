# 6.43. Даны числа a1,a2,...,a10. Определить сумму их квадратов.

import random

def calculate_func():
    sum = 0

    for i in range(1, 11):
        a = random.randint(0, 10)
        print(f"a{i} = {a}", end=" ")
        sum += a ** 2

    return sum


def main():
    sum_result = calculate_func()
    print(f"\nСумма квадратов чисел равна {sum_result:.2f}")


main()
