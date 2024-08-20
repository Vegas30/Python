import string
from itertools import permutations


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


# 19. Выделить гласные и согласные
# Напишите функцию, которая принимает строку и возвращает кортеж
# из двух списков: первый содержит все гласные буквы, второй —
# согласные.
# Пример: s = 'Hello World' → result = (['e', 'o', 'o'], ['H', 'l', 'l', 'W', 'r', 'l', 'd'])
def vowels_and_consonants(str):
    vowels = 'аоеиуюяэАОЕИУЮЯЭaeiouyAEIOUY'
    vovels_list = []
    consonants_list = []
    for char in str:
        if char.isalpha():
            if char in vowels:
                vovels_list.append(char)
            else:
                consonants_list.append(char)
    return vovels_list, consonants_list


# 20. Индексы всех вхождений символа
# Напишите функцию, которая возвращает список индексов всех
# вхождений заданного символа в строке.
# Пример: s = 'hello', char = 'l' → result = [2, 3]
def index_of_char(str, char):
    result_list = []
    str_list = enumerate(str)
    for index, value in str_list:
        if value == char:
            result_list.append(index)
    return result_list


# 21. Удаление дубликатов слов с сохранением порядка
# Напишите функцию, которая удаляет дубликаты слов из строки, сохраняя
# порядок их появления.
# Пример: s = 'hello world hello everyone' → s_result = 'hello world everyone'
def no_dublicate_in_string(str):
    new_str_list = []
    str_list = str.split()
    for word in str_list:
        if word not in new_str_list:
            new_str_list.append(word)
    result_str = " ".join(new_str_list)
    return result_str


# 22. Перестановка символов
# Напишите функцию, которая генерирует все возможные перестановки
# символов в строке.
# Пример: s = 'abc' → result = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
def char_permutat(str):
    perms = list(permutations(str))
    result = list(''.join(p) for p in perms)
    return result


# 23. Подсчет вхождений подстроки
# Напишите функцию, которая подсчитывает количество вхождений
# подстроки в строке без перекрытия.
# Пример: s = 'abcabc', sub = 'abc' → result = 2
def substring_count(str, sub):
    result = str.count(sub)
    return result


# 24. Создание аббревиатуры
# Напишите функцию, которая создает аббревиатуру из строки, сохраняя
# первую букву каждого слова в верхнем регистре.
# Пример: s = 'Hello World This Is Python' → result = 'HWTIP'
def make_abbreviation(str):
    words_list = str.split()
    result = ''
    for word in words_list:
        result += word[0].upper()
    return result


# 25. Сравнение двух строк с учетом частоты символов
# Напишите функцию, которая сравнивает две строки и возвращает True,
# если они имеют одинаковую частоту символов, и False в противном случае.
# Пример: s1 = 'aabbcc', s2 = 'abcabc' → result = True
def compare_string_frequency(s1, s2):
    if len(s1) != len(s2):
        return False
    char_freq_s1 = {}
    char_freq_s2 = {}

    for char in s1:
        char_freq_s1[char] = char_freq_s1.get(char, 0) + 1

    for char in s2:
        char_freq_s2[char] = char_freq_s2.get(char, 0) + 1

    return char_freq_s1 == char_freq_s2


# 26. Извлечение подстрок с заданной длиной
# Напишите функцию, которая извлекает все подстроки заданной длины из
# строки.
# Пример: s = 'abcde', length = 2 → result = ['ab', 'bc', 'cd', 'de']
def extract_substring_with_length(str, length):
    result = []
    # result = [str[i:i+length] for i in range(len(str) - length + 1)]
    for i in range(len(str) - length + 1):
        result.append(str[i:i + length])
    return result


# 27. Проверка строки на наличие цифр и букв
# Напишите функцию, которая проверяет, содержит ли строка хотя бы одну
# букву и хотя бы одну цифру.
# Пример: s = 'Hello123' → result = True
def check_string_for_letters_and_digits(str):
    has_letters = False
    has_number = False
    for char in str:
        if char.isalpha():
            has_letters = True
        if char.isalnum():
            has_number = True
        if has_letters and has_number:
            return True

    return False


# 28. Группировка символов по типу
# Напишите функцию, которая группирует символы строки по типу: буквы,
# цифры, специальные символы.
# Пример: s = 'abc123!@#' → result = {'letters': 'abc', 'digits': '123', 'special':
# '!@#'}
def group_by_type(str):
    group = {'letters': '', 'digits': '', 'specials': ''}
    for char in str:
        if char.isalpha():
            group['letters'] += char
        elif char.isdigit():
            group['digits'] += char
        else:
            group['specials'] += char
    return group


# 29. Удаление символов на основе условий
# Напишите функцию, которая удаляет из строки все символы, которые
# встречаются больше N раз.
# Пример: s = 'hello world', N = 2 → s_result = 'h wrd'
def remove_char_that_appear_more_N(str, n):
    char_count = {}
    s_result = ""
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1
    for char in str:
        if char_count[char] < n:
            s_result += char

    return s_result


# 30. Создание строки из ASCII-кодов
# Напишите функцию, которая принимает список ASCII-кодов и возвращает
# соответствующую строку.
# Пример: ascii_codes = [104, 101, 108, 108, 111] → result = 'hello'
def string_from_ASCII(lst):
    lst_string = ''.join([chr(elem) for elem in lst])
    return lst_string


# 31. Сжатие строки
# Напишите функцию, которая сжимает строку, заменяя последовательные
# одинаковые символы на символ и количество его повторений.
# Пример: s = 'aaabbc' → s_result = 'a3b2c1'
def string_compression(str):
    new_dict = {}
    for char in str:
        new_dict[char] = new_dict.get(char, 0) + 1
    result = ''.join([f'{key}{value}' for key, value in new_dict.items()])
    return result


# 32. Поиск самой длинной подстроки без повторяющихся символов
# Напишите функцию, которая находит самую длинную подстроку в строке
# без повторяющихся символов.
# Пример: s = 'abcabcbb' → result = 'abc'
def find_longest_string(str):
    pass


# 33. Создание маски для пароля
# Напишите функцию, которая создает маску для строки, заменяя все
# символы, кроме первого и последнего, на звездочки.
# Пример: s = 'password' → s_result = 'p******d'
def password_mask(str):
    new_str = str[0] + '*' * (len(str) - 2) + str[-1]
    return new_str


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
    print("4.", result)

    # 5. Объединить два списка без повторений
    list1 = ['x', 'y', 'z']
    list2 = ['y', 'z', 'a']
    res_list = union_two_lists(list1, list2)
    print("5.", res_list)

    # 6. Подсчет символов в строке
    s = 'hello world'
    result = char_count(s)
    print("6.", result)

    # 7. Первый и последний символ каждого слова
    s = "hello world"
    result = first_last_char(s)
    print("7.", result)

    # 8. Фильтрация по длине слов
    s = ['apple', 'banana', 'pear', 'kiwi']
    length = 4
    result = word_length_filter(s, length)
    print("8.", result)

    # 9. Сортировка слов по алфавиту
    s = ['banana', 'apple', 'cherry']
    result = char_sort(s)
    print("9.", result)

    # 10. Подсчет слов, начинающихся с заданной буквы
    s = 'apple apricot banana'
    letter = 'a'
    result = count_word_by_char(s, letter)
    print(f"10. String: {s}, letter = {letter}, count = {result}")

    # 11. Найти уникальные слова в строке
    s = 'hello Hello world world'
    result = uniq_word(s)
    print("11.", result)

    # 12. Перевод в нижний регистр
    s = ['Hello', 'WORLD']
    result = to_lower_list(s)
    print("12.", result)

    # 13. Объединение строк в одну
    s = ['apple', 'banana', 'cherry']
    s_result = union_list_to_stings(s) + "!"
    print("13.", s_result)

    # 14. Список чисел в строку
    list1 = [1, 2, 3]
    s_result = list_num_to_string(list1)
    print("14.", s_result)

    # 15. Преобразование строковых чисел в целые
    list1 = ['1', '2', '3']
    s_result = list_charnum_to_num(list1)
    print("15.", s_result)

    # 16. Добавить индекс к строкам
    s = ['apple', 'banana']
    s_result = index_to_string(s)
    print("16.", s_result)

    # 17. Нумерация строк
    list1 = ['First', 'Second', 'Third']
    s_result = string_numbering(list1)
    print("17.", s_result)

    # 18. Заменить символы на пробелы
    s = 'Hello, world!'
    char = ','
    s_result = replace_symbol_in_str(s, char)
    print("18.", s_result)

    # 19. Выделить гласные и согласные
    s = 'Hello World'
    result = vowels_and_consonants(s)
    print("19.", result)

    # 20. Индексы всех вхождений символа
    s = 'hello'
    char = 'l'
    result = index_of_char(s, char)
    print("20.", result)

    # 21. Удаление дубликатов слов с сохранением порядка
    s = 'hello world hello everyone'
    s_result = no_dublicate_in_string(s)
    print(s_result)

    # 22. Перестановка символов
    s = 'abc'
    result = char_permutat(s)
    print("22.", result)

    # 23. Подсчет вхождений подстроки
    s = 'abcabc'
    sub = 'abc'
    result = substring_count(s, sub)
    print("23.", result)

    # 24. Создание аббревиатуры
    s = 'Hello World This Is Python'
    result = make_abbreviation(s)
    print("24.", result)

    # 25. Сравнение двух строк с учетом частоты символов
    s1 = 'aabbcc'
    s2 = 'abcabc'
    result = compare_string_frequency(s1, s2)
    print("25.", result)

    # 26. Извлечение подстрок с заданной длиной
    s = 'abcde'
    length = 2
    result = extract_substring_with_length(s, length)
    print("26.", result)

    # 27. Проверка строки на наличие цифр и букв
    s = 'Hello123'
    result = check_string_for_letters_and_digits(s)
    print("27.", result)

    # 28. Группировка символов по типу
    s = 'abc123!@#'
    result = group_by_type(s)
    print("28.", result)

    # 29. Удаление символов на основе условий
    s = 'hello world'
    N = 2
    s_result = remove_char_that_appear_more_N(s, N)
    print("29.", s_result)

    # 30. Создание строки из ASCII-кодов
    ascii_codes = [104, 101, 108, 108, 111]
    result = string_from_ASCII(ascii_codes)
    print("30.", result)

    # 31. Сжатие строки
    s = 'aaabbc'
    s_result = string_compression(s)
    print("31.", s_result)

    # 32. Поиск самой длинной подстроки без повторяющихся символов
    s = 'abcabcbb'
    result = find_longest_string(s)
    print("32.", result)

    # 33. Создание маски для пароля
    s = 'password'
    s_result = password_mask(s)
    print("33.", s_result)


if __name__ == '__main__':
    main()
