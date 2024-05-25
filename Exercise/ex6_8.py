# 6.8. Дано число n. Из чисел 1, 4, 9, 16, 25, ... напечатать те, которые не
# превышают n.

def calculate_some(n):
    i = 1
    while i ** 2 <= n:
        print(i ** 2)
        i += 1


def main():
    num = int(input("Введите число n: "))
    calculate_some(num)


if __name__ == '__main__':
    main()
