# 7.2. Вывести на экран все целые числа от a до b, кратные некоторому
# числу c.

def print_multiples(a, b, c):
    for number in range(a, b + 1):
        if number % c == 0:
            print(number)


def main():
    a = int(input("Введите начальное значение a: "))
    b = int(input("Введите конечное значение b: "))
    c = int(input("Введите число c, кратное которому будем искать: "))

    print(f"Целые числа от {a} до {b}, кратные {c}:")
    print_multiples(a, b, c)


if __name__ == "__main__":
    main()
