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


#   print(num1, num2, num3)


# а)
def equal_all(a, b, c):
    if a == b == c:
        return True
    else:
        return False


print("Верно ли, что все его цифры одинаковые?:")
if equal_all(num1, num2, num3):
    print("Верно\n")
else:
    print("Не верно\n")


# б)
# первый способ
def equal_num(a, b, c):
    if a == b or a == c or b == c:
        return True
    else:
        return False


# второй способ
def equal_num2(a, b, c):
    if equal_all(a, b, c):
        print("Все числа одинаковые")
        return True, "", ""
    else:

        if a == b:
            return True, f"первое число {a}", f"второе число {b}"
        if a == c:
            return True, f"первое число {a}", f"третье число {c}"
        if b == c:
            return True, f"второе число {b}", f"третье число {c}"

        else:
            return False, "", ""


print("Определить, есть ли среди его цифр одинаковые.:")
bool_equal, num_equal1, num_equal2 = equal_num2(num1, num2, num3)
if bool_equal:
    print("Есть одинаковые:", num_equal1, num_equal2)
else:
    print("Нет одинаковых")
