# 6.38. Известны оценки абитуриента на четырех экзаменах.
# Определить сумму набранных им баллов.

def sum_numbers():
    summ = 0
    for i in range(1, 5):
        a = int(input("Введите оценку на экзамене: "))
        summ += a
    return summ


def main():
    result = sum_numbers()
    print("Сумма всех баллов =", result)


if __name__ == '__main__':
    main()
