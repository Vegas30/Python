# 5. Напиши функцию, которая удаляет все пустые строки из файла и записывает
# результат в новый файл.

def remove_str_lines(source_name: str, new_file: str) -> None:
    # with open(source_name,'r', encoding = 'utf-8') as file:
    #     with open(new_file, 'w', encoding= 'utf-8') as wfile:
    #             for line in file:
    #                 if line.strip():
    #                     wfile.write(line)
    with open(source_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(new_file, 'w', encoding='utf-8') as wfile:
        wfile.writelines(line for line in lines if line.strip())

#6. Функция, которая читает файл и подсчитывает количество символов (включая пробелы).
with open('source.txt','r',encoding='utf-8') as file:
    print(sum(len(line) for line in file))
    #print(len(file.read())

#7. Функция заменяет одно слово на другое.
with open('source.txt','r',encoding='utf-8') as file:
    content = file.read().replace('is','Python')
with open('source.txt','w', encoding='utf-8') as file:
    file.write(content)

#8. Функция, которая объединяет содержимое двух файлов в один.
import shutil
with open('itog.txt', 'w', encoding= 'utf-8') as file:
    for filename in ['source.txt','exp.txt']:
        with open(filename,'r', encoding='utf-8') as file2:
            #file.write(file2.read() + '\n')
            shutil.copyfileobj(file2, file)

def main():
    source_name = 'source.txt'
    new_file = 'remove_empty.txt'
    remove_str_lines(source_name, new_file)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print("Произошла ошибка - ", e)
    except (IOError, OSError) as e:
        print("Ошибка файла! - ", e)
    except FileNotFoundError as e:
        print("Файл не найден!", e)
    except PermissionError as e:
        print("Нет доступа к катологу!", e)

