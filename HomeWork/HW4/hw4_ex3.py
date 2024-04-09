# 3. Вычислить значение логического выражения при следующих
# значениях логических величин А, В и С: А = Истина, В = Ложь, С = Ложь:
# 1) А или В и не С;
# 2) А и не В или С;
# 3) не А и не В;
# 4) А и (не В или С);
# 5) не (А и С) или В;
# 6) А или (не (В и С)).

a = True
b = False
c = False

result_1 = a or (b and (not c)) # True
result_2 = a and (not b) or c   # True
result_3 = not a and not b      # False
result_4 = a and (not b or c)   # True
result_5 = not (a and c) or b   # True
result_6 = a or (not (b and c)) # True

print(result_1, result_2, result_3, result_4, result_5, result_6, sep="\n")

