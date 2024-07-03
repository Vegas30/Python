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


def high_temp_filter(month, t):
    new_array = list(filter(lambda x: t < x, month))
    return new_array


def celsius_to_fahrenheit(month):
    # (100 °C × 9/5) + 32 = 212 °F
    temp_in_fahrenheit = [celsius * 1.8 for celsius in month]
    return temp_in_fahrenheit


def any_day_high_level_temp(month, t):
    if any(list(filter(lambda x: x > t, month))):
        print("Верно, был хотя бы один день с температурой выше заданного значения")
    else:
        print("Не верно, не было хотя бы одного дня с температурой выше заданного значения")


def all_days_high_level_temp(month, t):
    if all(list(filter(lambda x: x > t, month))):
        print("Верно, все дни с температурой выше заданного значения")
    else:
        print("Не Верно, не все дни с температурой выше заданного значения")


def month_sort_min_max():
    pass


def print_menu():
    print("\nМеню:")
    print("1. Найти индекс первого дня, когда температура превысила заданное значение.")
    print("2. Найти индекс последнего дня, когда температура не превышала заданное значение.")
    print("3. Подсчитать количество дней, когда температура была ниже заданного значения.")
    print("4. Добавить в список температур еще один список температур за последние несколько дней месяца.")
    print("5. Удалить температуру последнего дня из списка.")
    print("6. Объединить два списка температур, представляющих собой данные двух разных месяцев.")
    print("7. Отфильтровать список, оставив только температуры, превышающие заданное значение.")
    print("8. Преобразовать список температур из Цельсия в Фаренгейты.")
    print("9. Проверить, был ли хотя бы один день с температурой выше заданного значения.")
    print("10.Проверить, были ли все дни с температурой выше заданного значения.")
    print("11.Очистить список температур.")
    print("12.Отсортировать список температур по возрастанию или убыванию (на основе любого выбранного вами ключа).")
    print("13.Подсчитать общее количество дней (элементов) в списке температур.")
    print("14.Выйти из программы")


def main():
    first_month = [random.randint(-2, 7) for _ in range(30)]
    print("Температура по дням: ", first_month)
    while True:
        print_menu()
        choice = input("Выберите действие от 1 до 14: ")
        if choice == '1':
            t = int(input("Введите значение температуры: "))
            index_of_first_day = first_day_index(first_month, t)
            print(f"Индекс первого дня, когда температура превысила заданное значение: {index_of_first_day}")
        elif choice == '2':
            t = int(input("Введите значение температуры: "))
            index_of_last_day = last_day_index(first_month, t)
            print(f"Индекс последнего дня, когда температура не превышала заданное значение.: {index_of_last_day}")
        elif choice == '3':
            t = int(input("Введите значение температуры: "))
            index_of_last_day = low_tmp_days_amount(first_month, t)
            print(f"Индекс последнего дня, когда температура не превышала заданное значение.: {index_of_last_day}")
        elif choice == '4':
            n = int(input("Введите количество дней для добавления: "))
            result_array = add_few_days(first_month, n)
            print(f"Список температур с добавленными днями.: {result_array}")
        elif choice == '5':
            result_array = del_last_day(first_month)
            print(f"Список температур с удаленной температурой последнего дня.: {result_array}")
        elif choice == '6':
            second_month = [random.randint(-2, 7) for _ in range(31)]
            print("Температура второго месяца по дням: ", second_month)
            new_array = first_month.extend(second_month)
            print(
                f"Новый список после объединения двух списков температур, представляющих собой данные двух разных месяцев: {new_array}")
        elif choice == '7':
            t = int(input("Введите значение температуры: "))
            result_array = high_temp_filter(first_month, t)
            print(f"Отфильтрованный список, с температурами, превышающими заданное значение.: {result_array}")
        elif choice == '11':
            print("Температура месяца по дням: ", first_month)
            accept = input(
                "Внимание основной список температур будет очищен и программа будет завершена, для подтверждения нажмите [y] или любую клавишу для продолжения")
            if accept == 'y':
                first_month.clear()
                print("Температура месяца по дням: ", first_month)
                break
            else:
                continue
        elif choice == '12':
            sorted_month = sorted(first_month, key=abs)
            print("Температуры сортируются по их абсолютному значению: \n", sorted_month)
        elif choice == '13':
            days_amount = len(first_month)
            print("Общее количество дней (элементов) в списке температур: ", days_amount)

        elif choice == '3':
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова")


if __name__ == '__main__':
    main()
