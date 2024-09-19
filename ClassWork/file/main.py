# 1. Напишите программу, которая читает текстовый файл и подсчитывает
# количество строк в нем. Предварительно создайте файл и
# запишите туда какие-либо данные.

# 2. Напишите программу, которая читает текстовый файл и подсчитывает количество слов
# в нем.

# 3. Напишите функцию, которая копирует содержимое одного файла в другой.
import shutil

shutil.copy('exp.txt', 'copy_2.txt')


# 4. Напишите функцию, которая читает первые n строк файла и выводит их на экран.
def read_first_n_lines_z4(n: int) -> None:
    with open('copy.txt', 'r', encoding='utf-8') as file:
        for _ in range(n):
            print(file.readline())



def copy_file_z3(filename: str, filename2: str) -> None:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    with open(filename2, 'w', encoding='utf-8') as file:
        file.write(content)


def count_words_z2():
    try:
        with open('exp.txt', 'r', encoding="utf-8") as file:
            # words = 0
            # for line in file:
            #     words += len(line.split())
            # return words
            return sum(len(line.split()) for line in file)
    except FileNotFoundError as e:
        print("Файл не найден.", e)
    except (IOError, OSError) as e:
        print("Ошибка доступа или памяти", e)


def append_lines(filename: str) -> None:
    try:
        with open(filename, 'w', encoding="utf-8") as file:
            while (line := input("Введите строку (exit для выхода): ")) != 'exit':
                file.write(line + '\n')
    except PermissionError as e:
        print("Нет прав к доступу или каталогу.", e)


def add_lines(filename: str) -> None:
    try:
        with open(filename, 'a', encoding="utf-8") as file:
            while (line := input("Введите строку (exit для выхода): ")) != 'exit':
                file.write(line + '\n')
    except PermissionError as e:
        print("Нет прав к доступу или каталогу.", e)


def count_lines_1z(filename: str) -> int:
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return len(file.readlines())
    except FileNotFoundError as e:
        print("Файл не найден.", e)
    except (IOError, OSError) as e:
        print("Ошибка доступа или памяти", e)


def main():
    filename = 'exp.txt'
    copy_file = input("Введите имя файла, в которой будет скопирован файл 'exp.txt'") + '.txt'
    # append_lines(filename)
    # add_lines(filename)
    print(f"Количество строк в файле: {count_lines_1z(filename)}")
    print(f"Количество слов в файле: {count_words_z2()}")
    copy_file_z3(filename, copy_file)

    n = int(input("Введите сколько первых строк вы хотите прочитать: "))
    read_first_n_lines_z4(n)


if __name__ == "__main__":
    main()
