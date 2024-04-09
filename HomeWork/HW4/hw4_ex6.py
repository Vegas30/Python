# 6. Вычислить значение логического выражения при следующих
# значениях логических величин А, В и С: А = Ложь, В = Ложь, С = Истина:
# а) (не А или не В) и не С;
# б) (не А или не В) и (А или В);
# в) А и В или А и С или не С.

a = False
b = False
c = True

res_1 = (not a or not b) and not c      # False
res_2 = (not a or not b) and (a or b)   # False
res_3 = a and b or a and c or not c     # False

print(res_1, res_2, res_3, sep="\n")
