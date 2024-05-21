# 6.2. Дана непустая последовательность неотрицательных целых
# чисел, оканчивающаяся отрицательным числом. Найти среднее
# арифметическое всех чисел последовательности (без учета
# отрицательного числа).

def calculte_func():
    sum = 0
    count = 0
    while True:
        n = int(input("Введите целое число: "))
        if n < 0:
            break
        sum += n
        count += 1
    res = sum / count
    return res


def calculte_func2():
    sum = 0
    count = 0
    n = int(input("Введите целое число: "))
    while n > 0:
        sum += n
        count += 1
        n = int(input("Введите целое число: "))
    res = sum / count
    return res


def main():
    result = calculte_func()
    print(round(result, 2))


main()
