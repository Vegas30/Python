# 6.33. Вычислить сумму при x = 2 .

def calculate_func(x):
    summ = 1
    denumerator = 2
    sign = -1
    for i in range(1, 13):
        summ += sign * ((i / denumerator) ** x)
        sign = sign * (-1)
        denumerator += 1
    return summ


def main():
    x = 2
    sum_result = calculate_func(x)
    print(f"Сумма при x = {x} равна {sum_result:.2f}")


main()
