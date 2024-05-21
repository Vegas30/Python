def average_from_1_to_1000():
    sum_numbers = 0
    count = 0
    for i in range(1, 1000 + 1):
        sum_numbers += i
        count += 1
    average_numbers = sum_numbers / count
    print(f"Среднее арифметическое всех целых чисел от 1 до 1000 равно {average_numbers}")


def average_from_100_to_b(b):
    if not (b >= 100):
        print("При таких значении переменной условие задачи неверно")
        return
    sum_numbers = 0
    count = 0
    for i in range(100, b + 1):
        sum_numbers += i
        count += 1
    average_numbers = sum_numbers / count
    print(f"Среднее арифметическое всех целых чисел от 100 до {b} равно {average_numbers}")


def average_from_a_to_200(a):
    if not (a <= 200):
        print("При таких значении переменной условие задачи неверно")
        return
    sum_numbers = 0
    count = 0
    for i in range(a, 200 + 1):
        sum_numbers += i
        count += 1
    average_numbers = sum_numbers / count
    print(f"Среднее арифметическое всех целых чисел от {a} до 200 равно {average_numbers}")


def average_from_a_to_b(a, b):
    if not (b >= a):
        print("При таких значении переменной условие задачи неверно")
        return
    sum_numbers = 0
    count = 0
    for i in range(a, b + 1):
        sum_numbers += i
        count += 1
    average_numbers = sum_numbers / count
    print(f"Среднее арифметическое всех целых чисел от {a} до {b} равно {average_numbers}")


def main():
    print("\n№ 6.20.")
    a = int(input("Введите целое число (a <= 200): "))
    b = int(input("Введите целое число (b >= 100): "))

    average_from_1_to_1000()
    average_from_100_to_b(b)
    average_from_a_to_200(a)
    average_from_a_to_b(a, b)


if __name__ == "__main__":
    main()
