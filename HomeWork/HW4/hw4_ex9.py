# 9. Вычислить значение логического выражения при всех возможных
# значениях логических величин А, В и С:
# а) не (А и В) и (не А или не С);
# б) не (А и не В) или (А или не С);
# в) А и не В или не (А или не С).

print("Первый способ решения задачи:")

print("\nа) не (А и В) и (не А или не С):")
print("A\t\tB\t\tC\t\tРезультат")
A, B, C = True, True, True
result = not (A and B) and (not A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = True, True, False
result = not (A and B) and (not A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = True, False, True
result = not (A and B) and (not A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = True, False, False
result = not (A and B) and (not A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, True, True
result = not (A and B) and (not A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, True, False
result = not (A and B) and (not A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, False, True
result = not (A and B) and (not A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, False, False
result = not (A and B) and (not A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")

print("\nб) не (А и не В) или (А или не С):")
print("A\t\tB\t\tC\t\tРезультат")
A, B, C = True, True, True
result = not (A and (not B)) or (A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = True, True, False
result = not (A and (not B)) or (A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = True, False, True
result = not (A and (not B)) or (A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = True, False, False
result = not (A and (not B)) or (A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, True, True
result = not (A and (not B)) or (A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, True, False
result = not (A and (not B)) or (A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, False, True
result = not (A and (not B)) or (A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, False, False
result = not (A and (not B)) or (A or (not C))
print(f"{A}\t{B}\t{C}\t{result}")

print("\nв) А и не В или не (А или не С):")
print("A\t\tB\t\tC\t\tРезультат")
A, B, C = True, True, True
result = A and (not B) or (not (A or (not C)))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = True, True, False
result = A and (not B) or (not (A or (not C)))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = True, False, True
result = A and (not B) or (not (A or (not C)))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = True, False, False
result = A and (not B) or (not (A or (not C)))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, True, True
result = A and (not B) or (not (A or (not C)))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, True, False
result = A and (not B) or (not (A or (not C)))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, False, True
result = A and (not B) or (not (A or (not C)))
print(f"{A}\t{B}\t{C}\t{result}")
A, B, C = False, False, False
result = A and (not B) or (not (A or (not C)))
print(f"{A}\t{B}\t{C}\t{result}")

print("\nВторой способ решения задачи:")
# Заголовки для результатов
print("\nа) не (А и В) и (не А или не С):")
print("A\t\tB\t\tC\t\tРезультат")

# Перебор всех комбинаций A, B и C
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            # Вычисление выражения а)
            result_a = not (A and B) and (not A or (not C))
            print(f"{A}\t{B}\t{C}\t{result_a}")

# Заголовки для результатов
print("\nб) не (А и не В) или (А или не С):")
print("A\t\tB\t\tC\t\tРезультат")

# Перебор всех комбинаций A, B и C
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            # Вычисление выражения б)
            result_b = not (A and (not B)) or (A or (not C))
            print(f"{A}\t{B}\t{C}\t{result_b}")

# Заголовки для результатов
print("\nв) А и не В или не (А или не С):")
print("A\t\tB\t\tC\t\tРезультат")

# Перебор всех комбинаций A, B и C
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            # Вычисление выражения в)
            result_c = A and (not B) or (not (A or (not C)))
            print(f"{A}\t{B}\t{C}\t{result_c}")
