
# 0. Создайте словарь через включение с несколькими ключами и значениями.
# Добавьте новый элемент в словарь. Удалите элемент из словаря. Измените
# значение существующего ключа. Получите значение по ключу.
lst = [2,3,'a',2.45]
dict1 = {i: lst[i] for i in range(len(lst))}
print(dict1)
dict2 = {k:v for k,v in enumerate(lst)}
print(dict2)
dict3 = {i: j for i in range(5) for j in "abcd"} #?
print(dict3)
dict4 = dict([('a',1), (2,3)])
print(dict4)

# Добавляем
dict1["Maxim"] = 60
print(dict1)

# Удаляем
dict1.popitem()
dict1.pop("Maxim")
del dict1["Maxim"]
print(dict1)

# Измение значения
dict1[0] = "Maxim"
print(dict1)

# Получение значения по ключу
print(dict1[1])

#Переберите все ключи и значения словаря с помощью цикла
for k in dict1.keys():
    print(k)

for k in dict1:
    print(k)

for v in dict1.values():
    print(v)

for k,v in dict1.items():
    print(f"{k}:{v}")

# 1. Создайте словарь, где ключ - это имена студентов, а значения -
# их оценки. Напишите функцию, которая принимает имя студента и новый балл,
# и обновляет его оценку в словаре.
def update_grades(students,name,grade):
    if name in students:
        students[name] = grade
    else:
        print("Увы такого нет студента")

def main():
    students = {'Maxim':59, 'Rasul': 75, 'Sergey': 78}
    name = input("Введите имя студента: ")
    grade = int(input("Введите новый балл: "))
    update_grades(students,name,grade)

# 2. Подсчитать количество букв в предложении
words = "Привет, как у тебя дела!У меня нормально!"
word_counts = {}

for word in words:
    word_counts[word] = word_counts.get(word,0) + 1
print(word_counts)

# 3. Напишите функцию, которая принимает два словаря и объединяет их.
# Если ключи совпадают, суммируйте их значение.
def merge_dict(dict1, dict2):
    merge = dict1.copy()
    for key, value in dict2.items():
        if key in merge:
            merge[key] += value
        else:
            merge[key] = value
    return merge

def main():
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    result_dict = merge_dict(dict1,dict2)
    print(result_dict)
main()

# 4. Напишите функцию, которая принимает словарь и возвращает новый словарь
# где ключи и значения поменяны местами.
dict1 = {'a': 1, 'b': 2, 'c': 3}
merge = {}
for key, value in dict1.items():
    merge[value] = key
print(merge)

merge = {value:key for key,value in dict1.items()}
print(merge)

# 5. Напишите функцию, которая удаляет из словаря все элементы с
# заданным значением
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
number = 3
for key, value in dict1.items():
    if value == number:
        del dict1[key]
#----------------------------------------------------------
key_to_remove = {key for key, value in dict1.items() if value == number}
print(key_to_remove)

for key in key_to_remove:
    del dict1[key]


# 6. Напишите функцию, которая принимает два списка одинаковой длины и
# создает из них словарь, где элементы первого списка - ключи, а второго
# значения.

keys = ['a','b','c']
values = ['name',24,'age']

dict_result = dict(zip(keys,values))
print(list(zip(keys,values)))
print(dict_result)

new_dict = dict.fromkeys(keys,values[0])
print(new_dict)

# 7. Напишите функцию, которая принимает два словаря и объединяет их.
# Если ключи совпадают, выберите наибольшее значение.
def merge_dict(dict1,dict2):
    copy_dict1 = dict1.copy()
    for key, value in dict2.items():
        if key in copy_dict1:
            copy_dict1[key] = max(copy_dict1[key],value)
        else:
            copy_dict1[key] = value
    return copy_dict1

def main():
    dict1 = {'a': 1, 'b': 5, 'name': 3}
    dict2 = {'a': 5, 'b': 3, 'hello': 3}
    dict_result = merge_dict(dict1,dict2)
    print(dict_result)
main()

# 8. Напишите функцию, которая принимает словарь с именами студентов
# и их оценками. Функция должна возвращать студентов, у которых оценка
# выше среднего.

students = {"Maxim": 60, 'Bob': 85, 'Alice': 78, 'Alina': 68}

average = sum(students.values()) / len(students)
print(average)
result_list_student = {student for student,grade in students.items() if grade > average}
print(result_list_student)

# 9. Напишите функцию, которая возвращает словарь, где ключи - это имена
# студентов, а значения их средние оценки
students = [
    {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 92}},
    {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 75}},
    {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 95}}
]
result_dict = {}
for student in students:
    name = student['name']
    grade = student['grades']
    average = round(sum(grade.values()) / len(grade),3)
    result_dict[name] = average
print(result_dict)

# 10. Напишите функцию, которая принимает список чисел и возвращает
# словарь, где ключи - числа, а значения - их факториалы.
from math import factorial
nums = [1,2,3,4,5]

result = {num: factorial(num) for num in nums}
print(result)
result = dict(zip(nums,map(lambda x: factorial(x), nums)))
print(result)

result = (x**2 for x in range(1,15))

# 11. Напишите функцию, которая принимет список чисел и возвращает словарь,
# где ключи - 'even' и 'odd', а значения - списки четных и нечетных чисел
nums = [1,2,3,4,5,6]
# Итог: {even:[2,4,6], odd: [1,3,5]}
dict1 = {'even': [], 'odd': []}
for i in nums:
    if i % 2 == 0:
        dict1['even'].append(i)
    else:
        dict1['odd'].append(i)
print(dict1)

# 12. Напишите функцию, которая принимает словарь, где значения могут
# повторяться, и возвращает новый словарь, где ключи - уникальные
# значения из исходного словаря, а значения - списки ключей, соответ-
# ствующие этим значениям.

dict1 = {'a':1, 'b':2, 'c':1, 'd': 2, 'e':3}
#{1:['a','c'], 2: ['b','d'], 3: ['e']}
result_dict = {}
for key, value in dict1.items():
    if value in result_dict:
        result_dict[value].append(key)
    else:
        result_dict[value] = [key]
#-----------------------------------
result_dict = {}
for key, value in dict1.items():
    result_dict.setdefault(key, []).append(value)
print(result_dict)
#---------------------------------------
# result_dict = {}
# result = {result_dict[value].append(key) if value in result_dict else result_dict[value] = [key] for key, value in dict1.items()}

# 13. Напишите функцию, которая принимает список строк и группирует их
# по длине. Верните словарь, где ключи - это длины строк, а значения -
# cписки строк соответствующей длины.
strings = ['a', 'bb', 'ccc', 'dd', 'e', 'ffff']
#{1 : ['a','e'],...}

result_dict = {}
for i in strings:
    length = len(i)
    if length in result_dict:
        result_dict[length].append(i)
    else:
        result_dict[length] = [i]
print(result_dict)

# 14. Напишите функцию, которая принимает два словаря и возвращает
# новый словарь содержащий только те пары ключ-значение, которые есть
# в обоих словарях.

dict1 = {'a':1, 'b':2, 'c':3, 'g': 6}
dict2 = {'a':1, 'b':2, 'c':3, 'd': 4}

set1 = set(dict1)
set2 = set(dict2)
set_result = set1 & set2
print(set_result)

dict_result = {}
for key,value in dict1.items():
    if key in set_result:
        dict_result[key] = value
print(dict_result)

# 15. Напишите функцию, которая принимает список словарей с информацией
# о студентах и их оценками, и возвращает словарь, где ключи - предметы
# а значения - кортежи с минимальной и максимальной оценками по каждому
# предмету.
students = [
    {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 92}},
    {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 75}},
    {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 95}}
]
min_max = {}
for student in students:
    for subject, grade in student['grades'].items():
        if subject not in min_max:
            min_max[subject] = (grade,grade)
        else:
            current_min, current_max = min_max[subject]
            min_max[subject] = (min(grade, current_min), max(grade, current_max))
print(min_max)


# 16. Напишите функцию, которая принимает список словарей с информацией
# о студентах и их оценками, и возвращает словарь, где ключи - предметы
# а значения - средние оценки по предметам, округленные до ближайшего целого.
students = [
    {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 92}},
    {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 75, 'fizo': 30}},
    {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 95}}
] #{'math': ...}

subject_totals = {}
subject_counts = {}
for student in students:
    for subject, grade in student['grades'].items():
        if subject not in subject_totals and subject not in subject_counts:
            subject_totals[subject] = grade
            subject_counts[subject] = 1
        else:
            subject_totals[subject] = subject_totals[subject] + grade
            subject_counts[subject] = subject_counts[subject] + 1
result_dict = {subject: round(subject_totals[subject]/subject_counts[subject]) for subject in subject_totals}
print(result_dict)

subject_totals = {}
subject_counts = {}
for student in students:
    for subject, grade in student['grades'].items():
        subject_totals[subject] = subject_totals.get(subject,0) + grade
        subject_counts[subject] = subject_counts.get(subject,0) + 1
result_dict = {subject: round(subject_totals[subject]/subject_counts[subject]) for subject in subject_totals}
print(result_dict)


# 17. Напишите функцию, которая принимает список словарей, .., возвращает список
# имен студентов, которые сдали все предметы выше 50.
students = [
    {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 92}},
    {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 75, 'fizo': 30}},
    {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 95}}
]
#-------------------------------------------------------------
result = []
for student in students:
    if all(grade > 50 for grade in student['grades'].values()):
        result.append(student['name'])
print(result)
#-------------------------------------------------------------
result = []
for student in students:
    flag = True
    for grade in student['grades'].values():
        if grade < 50:
            flag = False
    if flag:
        result.append(student['name'])
print(result)
#------------------------------------------------------------
result = [student['name'] for student in students if all(grade > 50 for grade in student['grades'].values())]
print(result)

# 18. ..., и возвращает словарь, где ключи - предметы, а значения - общие суммы
# оценок по каждому предмету.
#{'math':255,..}
students = [
    {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 92}},
    {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 75, 'fizo': 30}},
    {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 95}}
]

subject_totals = {}
for student in students:
    for subject, grade in student['grades'].items():
        subject_totals[subject] = subject_totals.get(subject, 0) + grade

result = {subject: subject_totals[subject] for subject in subject_totals}
print(result)

# 19. ..., возвращает сводную таблицу в виде словаря, где ключи - названия предметов,
# а значения - словари, в которых ключи - имена студентов, а значения - их оценки.
#{'math':{'Alice': 90, ...,}, ...}
students = [
    {'name': 'Alice', 'age': 24, 'grades': {'math': 90, 'physics': 85, 'chemistry': 92}},
    {'name': 'Bob', 'age': 23, 'grades': {'math': 70, 'physics': 80, 'chemistry': 75, 'fizo': 30}},
    {'name': 'Charlie', 'age': 22, 'grades': {'math': 85, 'physics': 89, 'chemistry': 95}}
]
result_dict = {'math':{}}
for student in students:
    for subject, grade in student['grades'].items():
        if subject not in result_dict:
            result_dict[subject] = {}
        result_dict[subject][student['name']] = grade
print(result_dict)
#-----------------------------------------------------------------
