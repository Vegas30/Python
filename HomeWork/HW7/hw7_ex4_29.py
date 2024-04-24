# 4.29. Дано двузначное число. Определить:
# а) входит ли в него цифра 3;
# б) входит ли в него цифра а.

number = int(input("Введите двузначное число "))
if not (9 < number < 100):
    print("Число не является двузначным. Ошибка ввода.")
else:
    dig_1 = number // 10
    dig_2 = number % 10
    # а)
    if dig_1 or dig_2 == 3:
        print(f"в число {number} входит цифра 3")
    else:
        print(f"в число {number} не входит цифра 3")
    # в)
    a = int(input("Введите число a "))
    if dig_1 or dig_2 == a:
        print(f"в число {number} входит цифра a = {a}")
    else:
        print(f"в число {number} не входит цифра a = {a}")
