# 6.14. Рассчитать значения y для значений х, равных 4, 5, ..., 28
def calculate_y(x):
    t = x + 2
    y = 2 * (t ** 2) + 5.5 * t - 2
    return y


def calculate_and_print():
    for i in range(4, 29):
        result = calculate_y(i)
        print(f"при x = {i} y = {result}")


def main():
    calculate_and_print()


main()
