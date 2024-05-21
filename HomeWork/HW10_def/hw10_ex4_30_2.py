# 4.30. Дано трехзначное число. Определить:
# а) входят ли в него цифры 4 или 7;
# б) входят ли в него цифры 3, 6 или 9.


def check_digits(number):
    number_str = str(number)
    has_4_or_7 = '4' in number_str or '7' in number_str
    has_3_6_or_9 = '3' in number_str or '6' in number_str or '9' in number_str
    return has_4_or_7, has_3_6_or_9


def main():
    user_number = int(input("Введите трехзначное число: "))
    if 100 <= user_number <= 999:
        digits_4_or_7, digits_3_6_or_9 = check_digits(user_number)
        print(f"В число {user_number} входят цифры 4 или 7: {'да' if digits_4_or_7 else 'нет'}")
        print(f"В число {user_number} входят цифры 3, 6 или 9: {'да' if digits_3_6_or_9 else 'нет'}")
    else:
        print("Ошибка: Введено не трехзначное число.")


# Точка входа в программу
if __name__ == "__main__":
    main()
