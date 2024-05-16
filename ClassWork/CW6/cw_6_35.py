def sum_numbers(number):
    summ = 0
    for i in range(1, number + 1):
        a = int(input("Введите элемент последовательности: "))
        summ += a
    return summ


def main():
    n = int(input("Введите количество элементов последовательности: "))
    if n <= 0:
        print("Плохо")
    else:
        result = sum_numbers(n)
        print("Сумма всех элементов последовательности =", result)


if __name__ == '__main__':
    main()
