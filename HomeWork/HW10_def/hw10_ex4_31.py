# 4.31. Дано четырехзначное число. Определить:
# а) входит ли в него цифра 4;
# б) входит ли в него цифра b.


def find_number_str(number, digit):
    exist = False
    for num in str(number):
        if int(num) == digit:
            print(f"Цифра {digit} содержится в числе {number}")
            exist = True
    if not exist:
        print(f"Цифра {digit} не содержится в числе {number}")


def main():
    user_number = int(input("Введите четырехзначное число: "))
    if not (999 < user_number < 10000):
        print("Число не является четырехзначным. Ошибка ввода.")
    else:
        print("\nа) входит ли в него цифра 4:")
        find_number_str(user_number, 4)

        print("\nб) входит ли в него цифра b")
        b = int(input("Введите цифру b: "))
        find_number_str(user_number, b)


if __name__ == "__main__":
    main()
