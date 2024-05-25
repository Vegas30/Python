# 6.11. Напечатать таблицу умножения на число n (значение n вводится
# с клавиатуры; 1 n 9).

def multiplication_table(n):
    for i in range(1, 10):
        print(f"{n} * {i} = {n * i}")


def main():
    n = int(input("Введите число n для таблицы умножения (1 <= n <= 9): "))
    if 1 <= n <= 9:
        multiplication_table(n)
    else:
        print("Ошибка: число n должно быть в диапазоне от 1 до 9.")


if __name__ == "__main__":
    main()
