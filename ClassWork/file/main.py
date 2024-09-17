# Напишите программу которая читает текстовый файл и подсчитывает кол-во строк в нем.

def appenf_lines(file_name) -> None:
    try:
        with open(file_name, 'w', encoding="utf-8") as file:
            while (line := input("Введите строку (exit для выхода): ")) != 'exit':
                file.write(line + '\n')
    except FileNotFoundError as e:
        print("Файл не найден.", e)
    except (IOError, OSError) as e:
        print("Ошибка ")


def add_lines(file_name) -> None:
    try:
        with open(file_name, 'a', encoding="utf-8") as file:
            while (line := input("Введите строку (exit для выхода): ")) != 'exit':
                file.write(line + '\n')
    except FileNotFoundError as e:
        print("Файл не найден.", e)
    except (IOError, OSError) as e:
        print("Ошибка ")


def count_lines(file_name):
    count = 0
    with open(file_name, 'r') as file:
        for line in file:
            if line:
                count += 1
    return count


def count_words(file_name):
    count = 0
    with open(file_name, 'r', encoding="utf-8") as file:
        return sum(len(line.split()) for line in file)

    return list_file

# Напишите функцию которая копирует содержимое одного файла в другой
def copy_file(file1, file2):
    with open(file1, 'r', encoding="utf-8") as file:
        content = file.read()
    with open(file2, 'w', encoding="utf-8") as file:
        file.write(content)

def read_first_n_lines(file_name, n):
    with open(file_name, 'r', encoding="utf-8") as file:
        for _ in range(n):
            print(file.readline())


def main():
    filename = 'exp.txt'
    filename2 = 'exp2.txt'
    # appenf_lines(filename)
    # add_lines(filename)
    # print(count_lines(filename))
    # print(count_words(filename))
    copy_file(filename, filename2)

if __name__ == '__main__':
    main()
