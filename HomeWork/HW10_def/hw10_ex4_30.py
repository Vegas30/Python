# 4.30. Дано трехзначное число. Определить:
# а) входят ли в него цифры 4 или 7;
# б) входят ли в него цифры 3, 6 или 9.


def find_number_str(number, *digits):
    exist = False
    for num in str(number):
        for digit in digits:
            if int(num) == digit:
                print(f"Цифра {digit} содержится в числе {number}")
                exist = True
    if not exist:
        print(f"Цифры {digits} не содержится в числе {number}")


def main():
    user_number = int(input("Введите трехзначное число: "))
    if not (99 < user_number < 1000):
        print("Число не является трехзначным. Ошибка ввода.")
    else:
        print("\nа) входят ли в него цифры 4 или 7:")
        find_number_str(user_number, 4, 7)
        print("\nб) входят ли в него цифры 3, 6 или 9")
        find_number_str(user_number, 3, 6, 9)


if __name__ == "__main__":
    main()
