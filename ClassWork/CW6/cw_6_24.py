# 6.24. Найти:
# а) произведение всех целых чисел от 8 до 15;
# б) произведение всех целых чисел от a до 20 (значение a вводится с
# клавиатуры; 1 <= a <= 20);
# в) произведение всех целых чисел от 1 до b (значение b вводится с
# клавиатуры; 1 <= b <= 20);
# г) произведение всех целых чисел от a до b (значения a и b вводятся с
# клавиатуры; b >= a).

def product_numbers_8_to_15():
    result = 1
    for i in range(8, 15 + 1):
        result *= i

    print(f"a) Произведение всех целых чисел от 8 до 15 равно {result}")


def product_numbers_a_to_20(a):
    result = 1
    for i in range(a, 21):
        result *= i
    print("б) Произведение всех целых чисел от", a, "до 20:", result)


def product_numbers_1_to_b(b):
    result = 1
    for i in range(1, b + 1):
        result *= i
    print("в) Произведение всех целых чисел от 1 до", b, ":", result)


def product_numbers_a_to_b(a, b):
    result = 1
    for i in range(a, b + 1):  # b + 1 потому что верхняя граница в range не включается
        result *= i
    print("г) Произведение всех целых чисел от", a, "до", b, ":", result)


def main():
    print("\n№ 6.24.")
    a = int(input("Введите целое число a от 1 до 20: "))
    b = int(input("Введите целое число b от 1 до 20: "))

    product_numbers_8_to_15()
    product_numbers_a_to_20(a)
    product_numbers_1_to_b(b)
    product_numbers_a_to_b(a, b)

if __name__ == "__main__":
    main()
