# 1. Дана строка. Перевернуть строку.
s = 'hello'
s_list = list(s)
print(s_list)
s_list.reverse()
print(s_list)
s_reverse = ''.join(s_list)
print(s_reverse)
#--------------------
s_reverse = s[::-1]
print(s_reverse)

# 2. Подсчитать количество гласных букв в слове

s = 'Привет, Максим! Как дела?'
glas = 'аоеиуюяэАОЕИУЮЯЭ'
result = len([i for i in s if i in glas])
#-------------------------------------
result = sum(1 for i in s if i in glas)
#-------------------------------------
num = set()
counts = 0
for i in s:
    if i in glas and i not in num:
        counts += s.count(i)
        num.add(i)
print(counts)

# 3. Удалить пробелы из строки
s = "Hello world! I world"
s_result = s.replace(" ", "")
print(s_result)

# 4. Заменить регистр всех букв на противоположный
s = 'HELLO world'
s_result = s.swapcase()
print(s_result)

# 5. Объединить списки
list1 = ['a','b','c']
list2 = ['a','c','d']
#list3 = ['a','b','c','d']

result = list(set(list1) | set(list2))
print(result)
#-----------------------------------
result = list(set(list1 + list2))
print(result)
#----------------------------------
list3 = []
for i in list1:
    for j in list2:
        if i not in list3:
            list3.append(i)
        if j not in list3:
            list3.append(j)
print(list3)

# 6. Напишите функцию, которая считает количество каждого символа в строке.
def char_count(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
s = " Напишите функцию, которая считает количество каждого символа в строке."
char_count(s)
#------------------------------
count = {}
for char in s:
    count[char] = count.get(char,0) + 1
print(count)
#------------------------------


#7. Напишите функцию, которая возвращает строку, состоящую из первых букв каждого
# слова в предложении.
s = "hello world python" #"hwp"
words = s.split()
result = ''
for word in words:
    result += word[0] #h+w+p -> hwp
print(result)

result = ''.join(char[0] for char in s.split())
#hello world python -> ['hello','world','python']
print(result)

#8. Программа, которая принимает список слов и возвращает новый список,содержащий
# только слова определенной длины.
s = ['hello', 'world', 'python', 'is']
length = 5

result = [i for i in s if len(i) == length]
result = list(filter(lambda x: len(x) == length, s))
print(result)

#9. Напишите, функцию которая сортирует список строк по их длине.
s = ['apple', 'fig', 'banana', 'cherry']
s_sort = sorted(s, key=len, reverse=True)

# 10. Напишите функцию, которая подсчитывает количество слов в списке,
# начинающихся с заданной буквы.
s = ['apple', 'banana', 'apricot', 'cherry']
letter = input("Введите букву с которой будем искать слова: ")
s_result = sum(1 for i in s if i.startswith(letter))
print(s_result)

# 11. Напишите функцию, которая принимает строку и возвращает список уникальных
# слов
s = 'hello world hello'
list1 = []
list2 = s.split()
for i in list2:
    if i not in list1:
        list1.append(i)

s_result = list(set(s.split()))
print(s_result)

# 12. Создайте функцию, которая переводит все строки в списке в верхний регистр
s = ['hello', 'world']
s_result = [i.upper() for i in s]
print(s_result)

# 13. Напиши функцию, которая принимает список строк и объединяет их в одну
# строку. И в конце поставить точку.
s = ['apple', 'banana', 'cherry']
#'apple, banana, cherry'
s_result = ', '.join(s) + '.'
print(s_result)

# 14. Напишите функцию, которая принимает список чисел и возвращает строку,
# содержащую эти числа, разделенные пробелами.
list1 = [1,2,3,4,5]
#'1 2 3 4 5'
s_result = ' '.join(map(str, list1))
print(s_result)

# 15. Напишите функцию, которая принимает список строковых чисел и возвращает список,
# содержащий эти числа целого типа.
list1 = ['1','2','3','4','5']
s_result = list(map(int, list1))

# s = 'dwff123fbewb34'
# a = '0123456789'
# list1 = []
# for i in s:
#     if i in a:
#         list1.append(i)
# print(list1)

# 16. Напишите функцию, которая принимает список строк и возвращает одну строку,
# где каждая строка начинается с её индекса в квадратных скобках.
s = ['apple', 'banana', 'cherry']
# "[0] apple, [1] banana, [2] cherry"
s_result = ', '.join(f"[{index}] {values}" for index, values in enumerate(s))
print(s_result)

# 17. Напишите функцию, которая принимает список строк и возвращает одну строку,
# где каждая строка нумеруется
list1 = ['First line', 'Second line', 'Third line']
# 1: First line
# 2: Second line
# 3: Third line
s_result = '\n'.join(f"{idx+1}: {val}" for idx,val in enumerate(list1))
print(s_result)

dict1 = {}
for idx,val in enumerate(list1):
    dict1[idx+1] = val

print(dict1)


# 20. Дана строка 'Hello! world' поменять местами буквы в слове 'world'. Итоговая
#cтрока 'Hello! dlrow'

#1.
s = 'Hello! world'
s_res = s.split('! ')
s_res[1] = s_res[1][::-1]
s_res = '! '.join(s_res)
print(s_res)

#2.
s_res = s[12:6:-1]
s_res = s[:7] + s_res
print(s_res)

#3.
s_res = "Hello! " + 'world'[::-1]

# 21. Дана строка 'Hello world' получить индекс всех букв l
s = 'Hello world'
result = s.find('l')
result2 = s.rfind('l')
result3 = s.find('l',result+1)

list = []
start = -1
counts = s.count('l')
while counts > 0:
    result = s.find('l',start+1)
    list.append(result)
    start = result
    counts -= 1
print(list)

# 22. Дана строка. 'Привет мир!' получить список и строку всех гласных букв.
s = 'Привет мир!'
word = 'аоеиуэ'
result = [i for i in s if i in word]
print(result)

# 23. Программа, которая принимает список строк и возвращает словарь с количеством
# гласных и согласных в каждой строке. А ключом будет сама строка
list1 = ['привет', 'как дела', 'Хороший! день, хочу домой', 'отдых']
{'привет':{'гласных': 2, 'согласных': 4}}
word = 'аоуеиэый'
result = {}

for s in list1:
    count_glasnix = sum(1 for i in s if i in word)
    #count_soglas = len(s) - count_glasnix #если в строке нет пробелов и специальных символов
    count_soglas = sum(1 for i in s if i.isalpha() and i not in word)
    result[s] = {'согласные': count_soglas, 'гласные': count_glasnix}
print(result)

# 24. Найти пересечение слов в строках
str1 = 'hello world bee'
str2 = 'world is bee beautiful'
#world
str3 = list(set(str1.split()) & set(str2.split()))
print(str3)
str3 = list(set(str1) & set(str2))
print(str3)

# 25. Cравнить две строки по уникальным символам.
str1 = 'apple'
str2 = 'bananas'
result = len(set(str1)) == len(set(str2))
print(result)

# 26. Создать зеркальную строку.
s = 'Hello world' #'olleH dlrow'
result = ' '.join(word[::-1] for word in s.split())
print(result)

# 27. Форматировать строку через интерполяцию
st = 'Hellow {name}, you have {points} points.'
data = {'name': 'Alice', 'points':5}
result = st.format(**data) #name = Alice, points = 5
print(result)

# 28. Удалить дубликаты слов с сохранием порядка
s = 'hello world hello everyone world'

words = s.split()
result = []

for word in words:
    if word not in result:
        result.append(word)
result2 = ' '.join(result)
print(result2)

result = []
print(list([result.append(word) for word in words if word not in result]))
print(result)
result3 = ' '.join(result)
print(result3)

#29. Перестановка символов.
#abcd -> ['abcd', 'acbd', ...]
s = 'abcd'
from itertools import permutations

perm = list(permutations(s))
print(perm)
result = [''.join(p) for p in perm]
print(result)

# 30. Подсчет вхождений подстроки.
s = 'acaca'
sub = 'aca'
result = s.count('aca')
print(result)

# 31. Создание аббревиатуру
#1.
s = 'Hello world this is Python' #HwtiP -> HWTIP
s_2 = s.title()
print(s_2)
result = ''.join(i[0] for i in s_2.split())

list2 = []
for word in s_2.split():
    if word not in list2:
        list2.append(word[0])
result = ''.join(list2)

#2.
s = 'Hello world this is Python'
result = ''.join(i[0].upper() for i in s_2.split())

# 32. Извлечь подстроку с заданной длинной
s = 'abcde'
length = 3
#['ab','bc','cd','de']
result = [s[i:i+length] for i in range(len(s) - length + 1)]
print(result)

# 33. Проверить что в строке есть и цифры, и буквы
s = 'Hello123'
if s.isalnum():
    print("okey")
else:
    print("ne okey")

if s.isdigit():
    print("okey2")

