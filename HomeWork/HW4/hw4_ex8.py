# 8. Вычислить значение логического выражения при всех возможных
# значениях логических величин А, В и С:
# а) не (А или не В и С);
# б) А и не (В и не С);
# в) не (не А или В и С).

print("Первый способ решения задачи:")

print("а) не (А или не В и С):")
A, B, C = True, True, True
result = not (A or (not B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = True, True, False
result = not (A or (not B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = True, False, True
result = not (A or (not B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = True, False, False
result = not (A or (not B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, True, True
result = not (A or (not B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, True, False
result = not (A or (not B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, False, True
result = not (A or (not B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, False, False
result = not (A or (not B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")

print("б) А и не (В и не С):")
A, B, C = True, True, True
result = A and (not (B and not C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = True, True, False
result = A and (not (B and not C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = True, False, True
result = A and (not (B and not C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = True, False, False
result = A and (not (B and not C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, True, True
result = A and (not (B and not C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, True, False
result = A and (not (B and not C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, False, True
result = A and (not (B and not C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, False, False
result = A and (not (B and not C))
print(f"A={A}, B={B}, C={C}, результат={result}")

print("не (не А или В и С):")
A, B, C = True, True, True
result = not (not A or (B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = True, True, False
result = not (not A or (B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = True, False, True
result = not (not A or (B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = True, False, False
result = not (not A or (B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, True, True
result = not (not A or (B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, True, False
result = not (not A or (B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, False, True
result = not (not A or (B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")
A, B, C = False, False, False
result = not (not A or (B and C))
print(f"A={A}, B={B}, C={C}, результат={result}")

print("\nВторой способ решения задачи:")

print("а) не (А или не В и С):")
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            result = not (A or (not B and C))
            print(f"A={A}, B={B}, C={C}, результат={result}")

print("б) А и не (В и не С):")
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            result = A and (not (B and not C))
            print(f"A={A}, B={B}, C={C}, результат={result}")

print("в) не (не А или В и С):")
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            result = not (not A or (B and C))
            print(f"A={A}, B={B}, C={C}, результат={result}")
