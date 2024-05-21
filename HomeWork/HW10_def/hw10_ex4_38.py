# 4.38. Даны два числа. Если квадратный корень из второго числа
# меньше первого числа, то увеличить второе число в пять раз.
import math


def modify_second_number(first, second):
    if math.sqrt(second) < first:
        print("Число после УВЕЛИЧЕНИЯ его в пять раза: ", second * 5)
    else:
        print(f"Число {second} не изменило свое значение.")


def main():
    # Ввод чисел пользователем

    number1 = float(input("Введите значение первого числа: "))
    number2 = float(input("Введите значение второго числа: "))

    if number1 < 0 or number2 < 0:
        print("Ошибка: оба числа должны быть неотрицательными.")
    else:

        # Вызов функции и вывод результата
        modify_second_number(number1, number2)


if __name__ == "__main__":
    main()
