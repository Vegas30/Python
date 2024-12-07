# 1. Подсчёт символов в файле.
# Напишите программу, которая подсчитывает количество символов
# (включая пробелы) в текстовом файле.
def count_characters_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            character_count = len(content)
            return character_count
    except FileNotFoundError:
        return "Файл не найден."


# 2. Вывод строки по ключевому слову.
# Напишите программу, которая ищет строки в файле, содержащие
# заданное ключевое слово, и выводит их.
def search_keyword_in_file(file_path, keyword):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if keyword in line:
                    print("\t", line.strip())
    except FileNotFoundError:
        print("Файл не найден.")


# 3. Чтение и сравнение файлов.
# Напишите программу, которая сравнивает содержимое двух файлов
# и выводит сообщение, одинаковы ли они.
def compare_files(file1, file2):
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        content1 = f1.read()
        content2 = f2.read()
    if content1 == content2:
        return "Содержимое файлов одинаково."
    else:
        return "Содержимое файлов отличается."

# 4. Частотный анализ слов.
# Напишите программу, которая подсчитывает, сколько раз каждое
# слово встречается в тексте файла.
def word_frequency_analysis(file_path):
    word_count ={}

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read().lower()
        text = ''.join(char for char in text if char.isalpha() or char.isspace())
        words = text.split()
        for word in words:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
    sorted_dict = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))
    for word, count in sorted_dict.items():
        print(f"Слово: \"{word}\" встречается {count} раз.")

# 5. Фильтрация строк по длине.
# Напишите программу, которая читает строки из файла и записывает
# в новый файл только те строки, длина которых больше заданного
# значения.
def filter_strings_by_length(input_file, output_file, string_length):
    with open(input_file, 'r', encoding='utf-8') as file_in, open(output_file, 'w', encoding='utf-8') as file_out:
        for line in file_in:
            if len(line.strip()) > string_length:
                file_out.write(line)

# 6. Разделение файла на части.
# Напишите программу, которая делит файл на несколько файлов,
# каждый из которых содержит не более N строк.
def split_file_by_lines(input_file, output_name, max_lines):
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    num_files = -(-len(lines) // max_lines)  # Определяем количество файлов, округляя вверх
    # num_files = len(lines) // max_lines  # Определяем количество файлов, округляя вверх - другой способ
    # if len(lines) % max_lines != 0:
    #     num_files += 1
    files = []
    for i in range(num_files):
        output_file = f"{output_name}_{i + 1}.txt"
        files.append(output_file)
        start_idx = i * max_lines
        end_idx = min((i + 1) * max_lines, len(lines))

        with open(output_file, 'w', encoding='utf-8') as file_out:
            file_out.writelines(lines[start_idx:end_idx])

    return num_files, files
# 7. Удаление строк с цифрами.
# Напишите программу, которая удаляет все строки, содержащие хотя
# бы одну цифру.
def del_lines_with_digits(file_path):
    output_file_name = f'{file_path[:-4]}_no_digits.txt'
    with open(file_path, 'r', encoding='utf-8') as file, open(output_file_name, 'w', encoding='utf-8') as output_file:
        for line in file:
            if not any(char.isdigit() for char in line):
                output_file.write(line)
    return output_file_name
def main():
    # 1.
    file_path = "example.txt"
    # Вызов функции для подсчета символов в файле
    character_count = count_characters_in_file(file_path)
    print("1. Количество символов в файле:", character_count)

    # 2.
    file_path = "example.txt"
    # Ключевое слово для поиска
    # keyword = str(input("Введите ключевое слово для поиска: "))
    keyword = "файл"
    print(f"2. Вот строки содержащие ключевое слово {keyword}: ")
    print("------------------------------------------")
    search_keyword_in_file(file_path, keyword)
    print("------------------------------------------")
    # 3.
    file_path1 = "file1.txt"
    file_path2 = "file2.txt"
    result = compare_files(file_path1, file_path2)  # сравниваем два разных файла
    print("3. Сравниваем файлы с разным содержимым: ", result)
    result = compare_files(file_path, file_path1)  # сравниваем два одинаковых файла
    print("3. Сравниваем файлы с одинаковым содержимым: ", result)
    # 4.
    file_path = "example.txt"
    print("4. Вот, сколько раз каждое слово встречается в тексте файла.: ")
    word_frequency_analysis(file_path)
    # 5.
    input_file_path = "example.txt"
    output_file_path = "output.txt"
    print("5. Фильтрация строк по длине.")
    # Задаем длину строки
    # string_length = int(input("Введите длину строки: "))
    string_length = 50
    print(f"Файл со строками длина которых больше {string_length}: {output_file_path}")
    filter_strings_by_length(input_file_path, output_file_path, string_length)
    # 6.
    # Укажите путь к вашему входному файлу и его название, имя для выходных файлов
    # и максимальное количество строк в каждом файле
    input_file_path = 'example.txt'
    output_file_name = 'output_split'
    # max_lines_per_file = int(input("Введите количество строк: "))
    max_lines_per_file = 15
    num_files, files = split_file_by_lines(input_file_path, output_file_name, max_lines_per_file)
    print(f"6. При заданном кол-ве строк {max_lines_per_file} исходный файл {input_file_path}"
          f" поделится на файлы в кол-ве {num_files}.\nС именами:\n{'\n'.join(files)} ")
    # 7.
    file_path = "example.txt"
    result_file = del_lines_with_digits(file_path)
    print(f"7. Имя файла после удаления строк содержащих хотя бы одну цифру: {result_file}")

if __name__ == '__main__':
    main()
