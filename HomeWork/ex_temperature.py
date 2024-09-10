# Существует список чисел, представляющих собой дневные
# температуры (в градусах Цельсия) в течение одного месяца (30 дней).
# Ваша задача - реализовать несколько функций, которые выполняют
# следующие операции с этим списком температур:
# 1. Найти индекс первого дня, когда температура превысила заданное значение.
# 2. Найти индекс последнего дня, когда температура не превышала
# заданное значение.
# 3. Подсчитать количество дней, когда температура была ниже заданного значения.
# 4. Добавить в список температур еще один список температур за последние несколько дней месяца.
# 5. Удалить температуру последнего дня из списка.
# 6. Объединить два списка температур, представляющих собой данные двух разных месяцев.
# 7. Отфильтровать список, оставив только температуры, превышающие заданное значение.
# 8. Преобразовать список температур из Цельсия в Фаренгейты.
# 9. Проверить, был ли хотя бы один день с температурой выше заданного значения.
# 10. Проверить, были ли все дни с температурой выше заданного значения.
# 11. Очистить список температур.
# 12. Отсортировать список температур по возрастанию или убыванию (на
# основе любого выбранного вами ключа).
# 13. Подсчитать общее количество дней (элементов) в списке температур.
import random



# 1. Найти индекс первого дня, когда температура превысила заданное значение.
def first_day_index(month, t):
    for day in month:
        if day > t:
            index_of_day = month.index(day)
            return index_of_day


# 2. Найти индекс последнего дня, когда температура не превышала заданное значение.
def last_day_index(month, t):
    reversed_month = month[::-1]
    for day in reversed_month:
        if day < t:
            index_of_day = month.index(day)
            return index_of_day


# 3. Подсчитать количество дней, когда температура была ниже заданного значения.
def low_tmp_days_amount(month, t):
    result = sum(list(filter(lambda x: t > x, month)))
    return result


# 4. Добавить в список температур еще один список температур за последние несколько дней месяца.
def add_few_days(month, n):
    new_array = month + month[n:]
    return new_array


# 5. Удалить температуру последнего дня из списка.
def del_last_day(month):
    new_array = month[:]
    new_array.pop()
    return new_array


# 6. Объединить два списка температур, представляющих собой данные двух разных месяцев.

# Создаем второй месяц и заполняем его случайными температурами с заданным диапазоном
def make_second_month(n, m):
    new_month = [random.randint(n, m) for _ in range(31)]
    return new_month


def join_two_month(first_month, second_month):
    result_array = first_month.extend(second_month)
    return result_array


# 7. Отфильтровать список, оставив только температуры, превышающие заданное значение.
def high_temp_filter(month, t):
    new_array = list(filter(lambda x: t < x, month))
    return new_array


# 8. Преобразовать список температур из Цельсия в Фаренгейты.
def celsius_to_fahrenheit(month):
    # (100 °C × 9/5) + 32 = 212 °F
    temp_in_fahrenheit = [celsius * 1.8 for celsius in month]
    return temp_in_fahrenheit


# 9. Проверить, был ли хотя бы один день с температурой выше заданного значения.
def any_day_high_level_temp(month, t):
    if any(list(filter(lambda x: x > t, month))):
        print("Верно, был хотя бы один день с температурой выше заданного значения")
    else:
        print("Не верно, не было хотя бы одного дня с температурой выше заданного значения")


# 10. Проверить, были ли все дни с температурой выше заданного значения.
def all_days_high_level_temp(month, t):
    if all(list(filter(lambda x: x > t, month))):
        print("Верно, все дни с температурой выше заданного значения")
    else:
        print("Не Верно, не все дни с температурой выше заданного значения")


# 11. Очистить список температур.
def clear_temperature_list(month):
    month.clear()


# 12. Отсортировать список температур по возрастанию или убыванию (на
# основе любого выбранного вами ключа).

def sort_list_by_key(month: list[int], selected_key: callable) -> list[int]:
    sorted_month = sorted(month, key=selected_key)
    return sorted_month


# 13. Подсчитать общее количество дней (элементов) в списке температур.
def count_days_amount(month: list[int]):
    days_amount = len(month)
    return days_amount


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
    while True:
        print("\nТемпература по дням: ", first_month)
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
            second_month = make_second_month(-2, 7)
            print("Температура второго месяца по дням: ", second_month)
            new_array_of_two_month = join_two_month(first_month, second_month)
            print(
                f"Новый список после объединения двух списков температур, представляющих собой данные двух разных месяцев: {new_array_of_two_month}")
        elif choice == '7':
            t = int(input("Введите значение температуры: "))
            result_array = high_temp_filter(first_month, t)
            print(f"Отфильтрованный список, с температурами, превышающими заданное значение.: {result_array}")
        elif choice == '8':
            t = int(input("Введите значение температуры: "))
            result_array = high_temp_filter(first_month, t)
            print(f"Преобразовать список температур из Цельсия в Фаренгейты.: {result_array}")
        elif choice == '9':
            t = int(input("Введите значение температуры: "))
            any_day_high_level_temp(first_month, t)
        elif choice == '10':
            t = int(input("Введите значение температуры: "))
            all_days_high_level_temp(first_month, t)
        elif choice == '11':
            print("Температура месяца по дням: ", first_month)
            accept = input(
                "Внимание основной список температур будет очищен и программа будет завершена, для подтверждения нажмите [y] или любую клавишу для продолжения")
            if accept == 'y':
                clear_temperature_list(first_month)
                print("Температура месяца по дням: ", first_month)
                break
            else:
                continue
        elif choice == '12':
            result = sort_list_by_key(month=first_month, selected_key=abs)
            print("Температуры сортируются по ключу abs: \n", result)

        elif choice == '13':
            result = count_days_amount(month=first_month)
            print("Общее количество дней (элементов) в списке температур: ", result)

        elif choice == '14':
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод. Попробуйте снова")


if __name__ == '__main__':
    main()
