# Проверить наличие хотя бы одного положительного числа в списке
lists = [-5, -6, -6, 1, 2]
result = lambda x: any(i > 0 for i in x)
print(result(lists))

# Проверить что все элементы списка являются четными
lists = [-5, -6, -6, 1, 2]
result = lambda x: all(i % 2 == 0 for i in x)
print(result(lists))