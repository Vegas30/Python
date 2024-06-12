# 11.26. В массиве хранятся сведения о количестве осадков, выпавших
# за каждый день февраля. Определить среднедневное количество
# осадков в этом месяце.

import random


def input_array(n):
    array = []
    for _ in range(n):
        array.append(round(random.uniform(0, 2), 2))
    return array


def fallout_in_month(month_array):
    day_average = sum(month_array) / len(month_array)
    return day_average


def main():
    # test_array = [2, 2, 2, 2, 2]

    february = 29

    february_array = input_array(february)

    print(f"Массив с осадками: {february_array}")

    average_fallout = fallout_in_month(february_array)

    print(f"Cреднедневное количество осадков в этом месяце: {average_fallout:.2f}")


main()
