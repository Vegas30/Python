# Напишите функцию которая удаляет все пустые строки из файла и записывает результат в новый файл.

def remove_empty_lines(source_file, new_file):
    # with open('source.txt', 'r', encoding="utf-8") as file:
    #     with open('new_file', 'w', encoding="utf-8") as wfile:
    #         for line in file:
    #             if line.strip():
    #                 wfile.write(line)
    with open(source_file, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    with open(new_file, 'w', encoding="utf-8") as wfile:
        wfile.writelines(line for line in lines if line.strip())
    # with open(source_file, 'r+', encoding="utf-8") as file:
    #     file.seek(10, 2)



def main():
    source_name = 'source.txt'
    new_file = 'copy_source.txt'
    remove_empty_lines(source_name, new_file)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Произошла ошибка - ", e)
    except (IOError, OSError) as e:
        print("Ошибка ввода-вывода - ", e)
    except FileNotFoundError as e:
        print("Файл не найден! - ", e)

