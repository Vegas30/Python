# 4.35. Определить, является ли заданное шестизначное число
# счастливым. (Счастливым называют такое шестизначное число, что
# сумма его первых трех цифр равна сумме его последних трех цифр.)


def lucky_number(number):
    number_str = str(number)
    if int(number_str[0]) + int(number_str[1]) + int(number_str[2]) == int(number_str[3]) + int(number_str[4]) + int(
            number_str[5]):
        return True
    return False


def main():
    user_number = int(input("Введите шестизначное число: "))
    if not (99999 < user_number < 1000000):
        print("Число не является шестизначным. Ошибка ввода.")
    else:
        if lucky_number(user_number):
            print("Это шестизначное число является счастливым.")
        else:
            print("Это шестизначное число не является счастливым.")


# Точка входа в программу
if __name__ == "__main__":
    main()
