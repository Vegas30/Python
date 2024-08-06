s = "hello"
p = "12345.45"
result = s.encode()
print(result)
res = p.isnumeric()
print(res)

# Дана строка, перевернуть строку.
s = 'hello'
s_list = list(s)
print(s_list)
s_list.reverse()
print(s_list)
s_reverse = "".join(s_list)
print(s_reverse)
# -------------------------------
s_reverse = s[::-1]
print(s_reverse)

# 2. Подсчитать кол-во гласных букв в слове
s = 'Привет, Маским! Как дела?'
glas = 'ауоиэыяюеёАУОИЭЫЯЮЕЁ'
result = sum(1 for i in s if i in glas)
result = len([1 for i in s if i in glas])
print(result)

# 3. Удалить пробелы из строки
s = "Hello world! I world"
s_result = s.replace(" ", "")
print(s_result)

# 4. Заменить регистр всех букв на противоположный
s = "HELLO world!"
s_result = s.swapcase()
print(s_result)

# 5. Объединить списки
list1 = ['a', 'b', 'c']
list2 = ['a', 'c', 'd']
result = list(set(list1) | set(list2))
result = set(list1).union(set(list2))
print(result)

# 6. Напишите функцию, которая считает количество каждого символа в строке.
s = "Напишите функцию, которая считает количество каждого символа в строке."


def count_characters(string):
    character_count = {}
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count


result = count_characters(s)
print(result)
# -------------------
count = {}
for char in s:
    count[char] = count.get(char, 0) + 1
print(count)

# 7. НАпишите функцию, которая возвращает строку которая состоит из первых букв каждого слова
s = "hello world python"

s_result = ''.join(word[0] for word in s.split())
print(s_result)

# 8. Программа, которая принимает список слов и возвращает новый список,
# содержащий только слова определенной длины
s = ['hello', 'world', 'python', 'is']
length = 5
result = [word for word in s if len(word) == length]
print(result)
result = list(filter(lambda x: len(x) == length, s))

# 9. Напишите функцию, которая сортирует список по их длине.
s = ['apple', 'fig', 'orange', 'banana']
s_sort = sorted(s, key=len)
print(s_sort)

# 10. Напишите функцию, которая подсчитывает количество слов в списке, начинающихся с заданной буквы.
s = ['apple', 'fig', 'orange', 'banana', 'cherry']
letter = 'a'
s_result = sum(1 for i in s if i.startswith(letter))
print(s_result)

# 11. Напишите функцию, которая принимает строку и возвращает список уникальных слов
# s =

# 12. Создайте функцию, которая переводит все строки в списке в верхний регистр
s = ['hello', 'world']
s_result = [i.upper() for i in s]
print(s_result)

# 13. Напишите функцию, которая принимает список строк и объединяет их в одну строку.
s = ['apple', 'bannana', 'cherry']
s_result = ", ".join(s) + "."
print(s_result)

# 14. Напишите функцию, которая принимает список чисел и возвращает сроку,
# содержащую эти числа, разделенные пробелами
list1 = [1, 2, 3, 4, 5]
# 1 2 3 4 5
s_result = ' '.join(map(str, list1))
print(s_result)

# 15.
list1 = ['1', '2', '3', '4', '5']
s_result = list(map(int, list1))

# 16. Напишите функцию, которая принимает список строк и возвращает одну строку,
# где каждая строка начинается с её индекса в квадратных скобках.
s = ['apple', 'bannana', 'cherry']
# "[0] apple, [1] bannana, [2] cherry"

s_result = ', '.join(f"[{index}] {values}" for index, values in enumerate(s))
print(s_result)

# 17. Напишите функцию, которая принимает список строк и возвращает одну строку где каждая строка нумеруется
list1 = ['First line', 'Second line', 'Third line']
# 1: First line
# 2: Second line
# 3: Third line
s_result = "\n".join(f"{index+1}: {values}" for index, values in enumerate(s))
print(s_result)

dict1 = {}
for idx, val in enumerate(list1, 1):
    dict1[idx] = val

print(dict1)