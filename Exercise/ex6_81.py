def search(num, a, b):
    count_a = 0
    count_b = 0
    for item in str(num):
        if a == int(item):
            count_a += 1
        elif b == int(item):
            count_b += 1

    if count_a < count_b:
        return True
    return False


def main():
    num = int(input("Введите натуральное число: "))
    num_a = int(input("Введите число a: "))
    num_b = int(input("Введите число b: "))
    if num_a == num_b:
        print("Ошибка ввода!")
    else:
        if search(num, num_a, num_b):
            print("Верно!")
        else:
            print("Не верно!")


main()
