# 9. Вычислить значение логического выражения при всех возможных
# значениях логических величин А, В и С:
# а) не (А и В) и (не А или не С);
# б) не (А и не В) или (А или не С);
# в) А и не В или не (А или не С).

# Заголовки для результатов
print("а) не (А и В) и (не А или не С):")
print("A\t\tB\t\tC\t\tРезультат")

# Перебор всех комбинаций A, B и C
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            # Вычисление выражения а)
            result_a = not (A and B) and (not A or not C)
            print(f"{A}\t{B}\t{C}\t{result_a}")

# Заголовки для результатов
print("\nб) не (А и не В) или (А или не С):")
print("A\t\tB\t\tC\t\tРезультат")

# Перебор всех комбинаций A, B и C
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            # Вычисление выражения б)
            result_b = not (A and not B) or (A or not C)
            print(f"{A}\t{B}\t{C}\t{result_b}")

# Заголовки для результатов
print("\nв) А и не В или не (А или не С):")
print("A\t\tB\t\tC\t\tРезультат")

# Перебор всех комбинаций A, B и C
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            # Вычисление выражения в)
            result_c = A and not B or not (A or not C)
            print(f"{A}\t{B}\t{C}\t{result_c}")
