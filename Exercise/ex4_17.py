import random

# 4.17. Дано трехзначное число.
# а) Верно ли, что все его цифры одинаковые?
# б) Определить, есть ли среди его цифр одинаковые.

num_a = int(input("Введите трехзначное число: "))
if not (100 <= num_a <= 999):
    print("Не трехзначное число")
else:
    num1 = num_a // 100
    num2 = (num_a // 10) % 10
    num3 = num_a % 10
    print(num1, num2, num3)


# а)
def equal_all(num1, num2, num3):
    if num1 == num2 == num3:
        return True
    else:
        return False


if equal_all(num1, num2, num3):
    print("Верно")
else:
    print("Не верно")


# б)
def equal_num(a, b, c):
    if a == b or a == c or b == c:
        return True
    else:
        return False


def equal_num2(a, b, c):
    if a == b:
        return True, a, b
    else:
        return False


if equal_num2(num1, num2, num3):
    print("Есть одинаковые", )
else:
    print("Нет одинаковых")
