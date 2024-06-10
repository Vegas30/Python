# 11.27. В массиве хранятся сведения о количестве осадков, выпавших
# за каждый день сентября. Определить, сколько осадков выпадало в
# среднем за один день в первую, вторую и третью декады этого
# месяца.
import random


def input_array(n):
    array = []
    for _ in range(n):
        array.append(random.uniform(0, 2))
    return array


def fallout_in_decade(month_array, decade):
    day_start = 0
    day_stop = 0
    if decade == 1:
        day_start = 0
        day_stop = 10
        days = 10
    elif decade == 2:
        day_start = 10
        day_stop = 20
        days = 10
    elif decade == 3:
        day_start = 20
        day_stop = len(month_array)
        days = len(month_array) - 20
    else:
        print("Не правильно указана декада")
    summ = 0
    for i in range(day_start, day_stop):
        summ += month_array[i]
    average_fallout = summ / days
    return average_fallout


def main():
    september = 30

    # september_array = input_array(september)
    september_array = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]

    decade_1 = fallout_in_decade(september_array, 1)
    decade_2 = fallout_in_decade(september_array, 2)
    decade_3 = fallout_in_decade(september_array, 3)

    print(f"Массив с осадками: {september_array}")

    print(
        f"В среднем осадков выпадало за один день в первую: {decade_1}, вторую: {decade_2} и третью декады: {decade_3} этого месяца.")


main()
