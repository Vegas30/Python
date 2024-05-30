# 6.31. Вычислить сумму Условный оператор и
# операцию возведения в степень не использовать.

from random import randint


def calculate_func(n):
    sum = 0
    l = 1

    for i in range(1, n + 1):
        sum += l * (1 / i)
        l = l * (-1)

    return sum


def main():
    n = randint(1, 10)
    sum_result = calculate_func(n)
    print(f"Сумма при n = {n} равна {sum_result:.2f}")


main()
