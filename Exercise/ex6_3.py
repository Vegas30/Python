# 6.3. Дана последовательность из n вещественных чисел. Первое число
# в последовательности нечетное. Найти сумму всех идущих подряд в
# начале последовательности нечетных чисел. Условный оператор не
# использовать.

def calculte_func():
    summ = 0
    number = float(input())
    while int(number) % 2 != 0:
        summ += number
        number = float(input())
    return summ

def main():
    result = calculte_func()
    print(round(result, 2))


main()
