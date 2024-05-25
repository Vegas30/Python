# 4.39. Даны три целых числа. Вывести на экран те из них, которые
# являются четными.

def even_numbers(*numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)


def main():
    num1 = int(input("Введите первое целое число: "))
    num2 = int(input("Введите второе целое число: "))
    num3 = int(input("Введите третье целое число: "))

    even_numbers(num1, num2, num3)


if __name__ == "__main__":
    main()
