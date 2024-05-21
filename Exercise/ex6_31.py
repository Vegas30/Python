from random import randint


def calculate_func(n):
    sum = 0
    l = 1

    for i in range(1, n + 1):
        sum += l * (1 / i)
        l = l * (-1)
    print(sum)


def main():
    n = randint(1, 10)
    calculate_func(n)


main()
