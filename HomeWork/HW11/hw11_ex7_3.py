# 7.3. Найти сумму положительных нечетных чисел, меньших 50.

def sum_positive_odd_numbers_below_50():
    total_sum = 0
    for number in range(1, 50, 2):  # Перебираем все нечетные числа от 1 до 49
        total_sum += number
    return total_sum


def main():
    sum_result = sum_positive_odd_numbers_below_50()
    print("Сумма положительных нечетных чисел, меньших 50, равна:", sum_result)


if __name__ == "__main__":
    main()
