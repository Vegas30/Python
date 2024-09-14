
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
