# Запросите у пользователя три строки, представляющие три строки
# стихотворения. Выведите их на экран, разделяя каждую строку
# переносом строки (\n).

# Запрашиваем у пользователя три строки стихотворения
first_line = input("Введите первую строку стихотворения: ")
second_line = input("Введите вторую строку стихотворения: ")
third_line = input("Введите третью строку стихотворения: ")

# Выводим строки на экран, разделяя их переносом строки
print(first_line, second_line, third_line, sep="\n")
