# 8. Вычислить значение логического выражения при всех возможных
# значениях логических величин А, В и С:
# а) не (А или не В и С);
# б) А и не (В и не С);
# в) не (не А или В и С).

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
            result = A and not (B and not C)
            print(f"A={A}, B={B}, C={C}, результат={result}")

print("в) не (не А или В и С):")
for A in [True, False]:
    for B in [True, False]:
        for C in [True, False]:
            result = not (not A or (B and C))
            print(f"A={A}, B={B}, C={C}, результат={result}")
