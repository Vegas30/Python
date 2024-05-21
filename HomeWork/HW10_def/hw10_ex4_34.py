# 4.34. Дано натуральное число n (n <= 9999). Выяснить, различны ли
# все четыре цифры этого числа (с учетом четырех цифр). Например, в
# числе 3678 все цифры различны, в числе 0023 — нет.


def compare_digits_in_number(number):
    number_str = str(number)
    for i in range(len(number_str)):
        for j in range(i + 1, len(number_str)):
            if number_str[i] == number_str[j]:
                return False
    return True


def main():
    user_number = int(input("Введите четырехзначное число: "))
    if not (999 < user_number < 10000):
        print("Число не является четырехзначным. Ошибка ввода.")
    else:
        # Проверяем, различны ли все четыре цифры числа
        if compare_digits_in_number(user_number):
            print("Все четыре цифры числа различны.")
        else:
            print("Не все четыре цифры числа различны.")


# Точка входа в программу
if __name__ == "__main__":
    main()
