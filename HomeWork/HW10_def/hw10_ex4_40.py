# 4.40. Даны три вещественных числа. Возвести в квадрат те из них,
# значения которых неотрицательны.
import math


def square_number(*numbers):
    for number in numbers:
        if number > 0:
            print(f"Число {number} не отрицательно и будет возведено в квадрат: {number**2}")


def main():
    # Ввод чисел пользователем

    number1 = float(input("Введите значение первого числа: "))
    number2 = float(input("Введите значение второго числа: "))
    number3 = float(input("Введите значение третьего числа: "))

    # Вызов функции и вывод результата
    square_number(number1, number2, number3)


if __name__ == "__main__":
    main()
