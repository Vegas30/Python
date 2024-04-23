# 4.11. Дано двузначное число. Определить:
# а) является ли сумма его цифр двузначным числом;
# б) больше ли числа а сумма его цифр.

a = int(input("Введите двузначное число: "))
if not (10 <= a <= 99):
    print("Ошибка, число не двузначное")
else:
    digit_1 = a // 10
    digit_2 = a % 10
    # а) является ли сумма его цифр двузначным числом
    sum_of_digits = digit_1 + digit_2
    if 10 <= sum_of_digits <= 18:
        print(f"Сумма цифр числа ({a}) двузначное число.")
    else:
        print(f"Сумма цифр числа ({a}) не является двузначным числом.")
    # б) больше ли числа а сумма его цифр.
    if sum_of_digits > a:
        print(f"Сумма цифр числа ({a}) больше его самого")
    else:
        print(f"Сумма цифр числа ({a}) меньше его самого")

