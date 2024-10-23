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
def main():
    # 1.
    file_path = "example.txt"
    # Вызов функции для подсчета символов в файле
    character_count = count_characters_in_file(file_path)
    print("1. Количество символов в файле:", character_count)

    # 2.
    file_path = "example.txt"
    # Ключевое слово для поиска
    keyword = "файл"
    print("2. Вот строки содержащие ключевое слово: ")
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
    word_frequency_analysis(file_path)

if __name__ == '__main__':
    main()
