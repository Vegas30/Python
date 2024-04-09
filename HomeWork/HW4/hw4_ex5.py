# 5. Вычислить значение логического выражения при следующих
# значениях логических величин А, В и С: А = Истина, В = Ложь, С = Ложь:
# а) А или не (А и В) или С;
# б) не А или А и (В или С);
# в) (А или В и не С) и С.

a = True
b = False
c = False

res_1 = a or not (a and b) or c     # True
res_2 = not a or a and (b or c)     # False
res_3 = (a or b and not c) and c    # False

print(res_1,res_2,res_3, sep="\n")


