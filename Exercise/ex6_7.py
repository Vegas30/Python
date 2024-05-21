# 6.7. Дана непустая последовательность положительных целых чисел
# a1,a2,..., оканчивающаяся нулем. Получить a1, a1*a2, a1*a2*a3,.., 0.

def calculate_some():
    multiply = 1
    while True:
        number = int(input("Введите элемент последовательности: "))
        if number == 0:
            break
        multiply *= number
        print(multiply)


def main():
    calculate_some()


if __name__ == '__main__':
    main()
