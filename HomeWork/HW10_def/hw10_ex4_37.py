# 4.37. Составить программу, которая уменьшает первое введенное
# число в два раза, если оно больше второго введенного числа по
# абсолютной величине.

def adjust_number(first, second):
    if abs(first) > abs(second):
        if first < 0:
            first *= 2
            print("Число после УМЕНЬШЕНИЯ его в два раза: ", first)
        else:
            first /= 2
            print("Число после УМЕНЬШЕНИЯ его в два раза: ", first)
    else:
        print(f"Число {first} не изменило свое значение.")


def main():
    # Ввод чисел пользователем
    number1 = float(input("Введите значение первого числа: "))
    number2 = float(input("Введите значение второго числа: "))

    # Вызов функции и вывод результата
    adjust_number(number1, number2)


if __name__ == "__main__":
    main()
