# 6.32. Вычислить сумму при x = 2


def calculate_func(x):
    sum = 0

    for i in range(1, 12, 2):
        sum += (x ** i) / i
    return sum


def main():
    x = 2
    sum_result = calculate_func(x)
    print(f"Сумма при x = {x} равна {sum_result:.2f}")


main()
