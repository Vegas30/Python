import string


# 1. Перевернуть строку
# Дана строка. Напишите функцию, которая переворачивает слова в
# строке, сохраняя порядок слов.
# Пример: s = 'hello world' → s_result = 'olleh dlrow'
def revers_word_in_string(str):
    result = ' '.join(word[::-1] for word in str.split())
    return result


# 2. Подсчет гласных
# Напишите функцию, которая принимает строку и возвращает
# количество уникальных гласных букв.
def vowels_count(str):
    vowels = 'аоеиуюяэАОЕИУЮЯЭ'
    unique_vowels = set()
    for char in str:
        if char in vowels and char not in unique_vowels:
            unique_vowels.add(char.lower())
    return len(unique_vowels), unique_vowels


# 3. Удалить знаки препинания
# Дана строка с различными знаками препинания. Напишите
# функцию, которая удаляет все знаки препинания из строки.
# Пример: s = "Привет! Как дела?" → s_result = "Привет Как дела"
def del_punctuation(str):
    clean_string = ""

    for char in str:
        if char not in string.punctuation:
            clean_string += char

    return clean_string


# 4. Инвертировать регистр
# Напишите функцию, которая инвертирует регистр всех букв в
# строке.
# Пример: s = 'Python Programming' → s_result = 'pYTHON
# pROGRAMMING'
def invert_register(str):
    result = str.swapcase()
    return result


# 5. Объединить два списка без повторений
# Даны два списка. Напишите функцию, которая объединяет их,
# исключая повторяющиеся элементы и сохраняя порядок.
# Пример: list1 = ['x', 'y', 'z'], list2 = ['y', 'z', 'a'] → result = ['x', 'y', 'z', 'a']
def union_two_lists(list1, list2):
    result = list(set(list1 + list2))
    return result


# 6. Подсчет символов в строке
# Напишите функцию, которая подсчитывает количество каждого
# символа в строке, игнорируя пробелы.
# Пример: s = 'hello world' → result = {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1,
# 'd': 1}
def char_count(str):
    # new_dict = dict.fromkeys(str, 1)
    new_dict = {}
    for char in str.replace(" ", ""):
        new_dict[char] = new_dict.get(char, 0) + 1
    return new_dict


# 7. Первый символ каждого слова
# Напишите функцию, которая возвращает строку, состоящую из
# первых и последних букв каждого слова в предложении.
# Пример: s = "hello world" → result = "hlow"
def first_last_char(str):
    words = str.split()
    result = ''
    for word in words:
        result += word[0]
        result += word[len(word) - 1]
    return result


# 8. Фильтрация по длине слов
# Напишите функцию, которая принимает список слов и возвращает
# новый список, содержащий только слова, длина которых больше
# заданного числа.
# Пример: s = ['apple', 'banana', 'pear', 'kiwi'], length = 4 → result =
# ['apple', 'banana']
def word_length_filter(lst, length):
    new_list = []
    # for word in lst:
    #     if len(word) > 4:
    #         new_list.append(word)
    [new_list.append(word) for word in lst if len(word) > 4]
    return new_list


# 9. Сортировка слов по алфавиту
# Напишите функцию, которая сортирует список строк в алфавитном
# порядке.
# Пример: s = ['banana', 'apple', 'cherry'] → s_result = ['apple', 'banana',
# 'cherry']
def char_sort(lst):
    sorted_list = sorted(lst)
    return sorted_list


# 10. Подсчет слов, начинающихся с заданной буквы
# Напишите функцию, которая подсчитывает количество слов в
# строке, начинающихся с заданной буквы, без учета регистра.
# Пример: s = 'apple apricot banana', letter = 'a' → result = 2
def count_word_by_char(str, letter):
    count = 0
    for char in str:
        if char == letter:
            count += 1
    return count


# 11. Найти уникальные слова в строке
# Напишите функцию, которая принимает строку и возвращает список
# уникальных слов, игнорируя регистр.
# Пример: s = 'hello Hello world world' → result = ['hello', 'world']
def uniq_word(str):
    uniq_list = []
    # for word in str.lower().split():
    #     if word not in uniq_list:
    #         uniq_list.append(word)
    [uniq_list.append(word) for word in str.lower().split() if word not in uniq_list]
    return uniq_list


# 12. Перевод в нижний регистр
# Напишите функцию, которая переводит все строки в списке в нижний регистр.
# Пример: s = ['Hello', 'WORLD'] → s_result = ['hello', 'world']
def to_lower_list(lst):
    new_list = []
    for word in lst:
        new_list.append(word.lower())
    return new_list


# 13. Объединение строк в одну
# Напишите функцию, которая принимает список строк и объединяет
# их в одну строку, разделяя запятыми, и добавляет в конце
# восклицательный знак.
# Пример: s = ['apple', 'banana', 'cherry'] → s_result = 'apple, banana, cherry!'
def union_list_to_stings(lst):
    new_str = ', '.join(lst)
    return new_str


# 14. Список чисел в строку
# Напишите функцию, которая принимает список чисел и возвращает
# строку, содержащую эти числа, разделенные точками.
# Пример: list1 = [1, 2, 3] → s_result = '1.2.3'
def list_num_to_string(lst):
    # char_str = [str(num) for num in lst]
    res_str = '.'.join([str(num) for num in lst])
    return res_str

# 15. Преобразование строковых чисел в целые
# Напишите функцию, которая принимает список строковых чисел и
# возвращает список этих чисел в виде строк.
# Пример: list1 = ['1', '2', '3'] → s_result = [1, 2, 3]
def list_charnum_to_num(lst):
    res_list = [int(char) for char in lst]
    return res_list

# 16. Добавить индекс к строкам
# Напишите функцию, которая принимает список строк и возвращает
# одну строку, где каждая строка начинается с её индекса в квадратных
# скобках, и элементы разделены запятыми.
# Пример: s = ['apple', 'banana'] → s_result = '[0] apple, [1] banana'
def index_to_string(lst):
    result_str = ', '.join(f"[{index}] {values}" for index, values in enumerate(lst, start=1))
    return result_str

# 17. Нумерация строк
# Напишите функцию, которая принимает список строк и возвращает
# одну строку, где каждая строка нумеруется.
# Пример: list1 = ['First', 'Second', 'Third'] → s_result = '1: First\n2:
# Second\n3: Third'
def string_numbering(lst):
    result_str = '\n'.join(f"{index}: {values}" for index, values in enumerate(lst, start=1))
    return result_str

# 18. Заменить символы на пробелы
# Напишите функцию, которая заменяет все вхождения определённого
# символа в строке на пробелы.
# Пример: s = 'Hello, world!', char = ',' → s_result = 'Hello world!'
def replace_symbol_in_str(str, char):
    result_str = str.replace(char, " ")
    return result_str


def main():
    # 1. Перевернуть строку
    s = 'hello world'
    result = revers_word_in_string(s)
    print("1.", result)

    # 2. Подсчет гласных
    s = 'Привет, Максим! Как дела?'
    result_count, result_vowels = vowels_count(s)
    print(f"2. Количество гласных в строке ({s}) = {result_count}, (гласные: {', '.join(result_vowels)})")

    # 3. Удалить знаки препинания
    s = "Привет! Как дела?"
    result = del_punctuation(s)
    print("3.", result)

    # 4. Инвертировать регистр
    s = 'Python Programming'
    result = invert_register(s)
    print(result)

    # 5. Объединить два списка без повторений
    list1 = ['x', 'y', 'z']
    list2 = ['y', 'z', 'a']
    res_list = union_two_lists(list1, list2)
    print(res_list)

    # 6. Подсчет символов в строке
    s = 'hello world'
    result = char_count(s)
    print(result)

    # 7. Первый и последний символ каждого слова
    s = "hello world"
    result = first_last_char(s)
    print(result)

    # 8. Фильтрация по длине слов
    s = ['apple', 'banana', 'pear', 'kiwi']
    length = 4
    result = word_length_filter(s, length)
    print(result)

    # 9. Сортировка слов по алфавиту
    s = ['banana', 'apple', 'cherry']
    result = char_sort(s)
    print(result)

    # 10. Подсчет слов, начинающихся с заданной буквы
    s = 'apple apricot banana'
    letter = 'a'
    result = count_word_by_char(s, letter)
    print(f"String: {s}, letter = {letter}, count = {result}")

    # 11. Найти уникальные слова в строке
    s = 'hello Hello world world'
    result = uniq_word(s)
    print(result)

    # 12. Перевод в нижний регистр
    s = ['Hello', 'WORLD']
    result = to_lower_list(s)
    print(result)

    # 13. Объединение строк в одну
    s = ['apple', 'banana', 'cherry']
    s_result = union_list_to_stings(s) + "!"
    print(s_result)

    # 14. Список чисел в строку
    list1 = [1, 2, 3]
    s_result = list_num_to_string(list1)
    print(s_result)

    # 15. Преобразование строковых чисел в целые
    list1 = ['1', '2', '3']
    s_result = list_charnum_to_num(list1)
    print(s_result)

    # 16. Добавить индекс к строкам
    s = ['apple', 'banana']
    s_result = index_to_string(s)
    print(s_result)

    # 17. Нумерация строк
    list1 = ['First', 'Second', 'Third']
    s_result = string_numbering(list1)
    print(s_result)

    # 18. Заменить символы на пробелы
    s = 'Hello, world!'
    char = ','
    s_result = replace_symbol_in_str(s, char)
    print(s_result)


if __name__ == '__main__':
    main()
