# 2. Вычислить значение логического выражения при следующих
# значениях логических величин А, В и С: А = Истина, В = Ложь, С =
# Ложь:
# а) не А и В;
# б) А или не В;
# в) А и В или С.

a = True
b = False
c = False

result1 = not a and b  # False
result2 = a or (not b)  # True
result3 = (a and b) or c  # False

print(result1, result2, result3)
