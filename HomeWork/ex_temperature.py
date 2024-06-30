# Существует список чисел, представляющих собой дневные
# температуры (в градусах Цельсия) в течение одного месяца (30 дней).
# Ваша задача - реализовать несколько функций, которые выполняют
# следующие операции с этим списком температур:
# 1. Найти индекс первого дня, когда температура превысила заданное значение.
# 2. Найти индекс последнего дня, когда температура не превышала
# заданное значение.
# 3. Подсчитать количество дней, когда температура была ниже
# заданного значения.
# 4. Добавить в список температур еще один список температур за
# последние несколько дней месяца.
# 5. Удалить температуру последнего дня из списка.
# 6. Объединить два списка температур, представляющих собой данные
# двух разных месяцев.
# 7. Отфильтровать список, оставив только температуры, превышающие
# заданное значение.
# 8. Преобразовать список температур из Цельсия в Фаренгейты.
# 9. Проверить, был ли хотя бы один день с температурой выше
# заданного значения.
# 10.Проверить, были ли все дни с температурой выше заданного
# значения.
# 11.Очистить список температур.
# 12.Отсортировать список температур по возрастанию или убыванию (на
# основе любого выбранного вами ключа).
# 13.Подсчитать общее количество дней (элементов) в списке температур.
import random


def first_day_index(month, t):
    for day in month:
        if day > t:
            index_of_day = month.index(day)
            return index_of_day


def last_day_index(month, t):
    reversed_month = month[::-1]
    for day in reversed_month:
        if day < t:
            index_of_day = month.index(day)
            return index_of_day

def low_tmp_days_amount(month, t):
    result = sum(list(filter(lambda x: t > x, month)))
    return result

def add_few_days(month, n):
    new_array = month + month[n:]
    return new_array

def del_last_day(month):
    new_array = month[:]
    new_array.pop()
    return new_array



def print_menu():
    print("\nМеню:")
    print("1. Найти индекс первого дня, когда температура превысила заданное значение.")
    print("2. Удалить последний элемент из списка")
    print("3. Выйти из программы")


def main():
    temperature_by_days_array = [random.randint(-2, 7) for _ in range(30)]
    print("Температура по дням: ", temperature_by_days_array)
    while True:
        print_menu()
        choice = input("Выберите действие (1/2/3): ")
        print(type(choice))
        if choice == '1':
            index_of_first_day = first_day_index(temperature_by_days_array)
            print(f"Индекс первого дня, когда температура превысила заданное значение: {index_of_first_day}")
        elif choice == '2':
            nomer = int(input("Введите номер желаемого элемента: "))
            new_array = pop_array(main_array, nomer - 1)
            print(f"Новый список после удаления последнего элемента списка: {new_array}")
        elif choice == '3':
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова")


if __name__ == '__main__':
    main()
