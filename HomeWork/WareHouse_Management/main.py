# WareHouse_Management/main.py
from operations.file_operations import load_items_from_file, save_items_to_file, export_items_to_csv, \
    import_items_from_json
from operations.ware_operations import add_item, remove_item, find_items_by_location, filter_items_by_category_and_tags, \
    update_item_quantity, generate_warehouse_report, generate_unique_item_id
from operations.validation import validate_new_item_data, ValidationError
import csv
import json

FILE_PATH = "data/warehouse.json"


def load_items() -> list[dict]:
    """
    Вызываем функцию для загрузки товаров из файла JSON.

    :return: Список загруженных товаров.
    :rtype: list[dict]
    """
    return load_items_from_file(FILE_PATH) or []


def save_items(items: list[dict]) -> None:
    """
    Вызываем функцию для сохранения товаров в файл JSON

    :param items: Список товаров для сохранения.
    :type items: list[dict]
    """
    save_items_to_file(items, FILE_PATH)


def main():
    """Консольное приложение для управления складом товаров."""

    items = load_items()

    while True:
        print("\nПРИОЛЖЕНИЕ ПО УПРАВЛЕНИЮ СКЛАДОМ ТОВАРОВ")
        print("-" * 40)
        print("Выберите действие:")
        print("1. Добавление товара.")
        print("2. Удаление товара.")
        print("3. Фильтрация товара по категории и тегам.")
        print("4. Поиск товара по местоположению товара на складе.")
        print("5. Изменение количества товара.")
        print("6. Экспорт данных о товарах в CVS файл.")
        print("7. Импорт данных о товарах из JSON файла.")
        print("8. Генерация отчета о товарах на складе.")
        print("0. Выход из программы.")

        choice = input("Введите номер действия: ")
        if choice == "1":
            try:
                while not (new_name := input("Введите наименование товара, например Table: ")):
                    print("Наименование товара не может быть пустым.")
                while not (new_category := input("Введите категорию товара, например Furniture: ")):
                    print("Категория товара не может быть пустой.")
                while not (new_quantity := int(input("Введите количество товара в виде целого числа, например 8: "))):
                    print("Количество товара должно быть целым числом.")
                while not (new_price := round(float(input("Введите цену товара, например 150.50: ")), 2)):
                    print("Цена товара должна быть числом.")
                while not (new_tags := list(set(input("Введите метки товара (tags) через запятую, например office, sale: ").split(', ')))):
                    print("Метки товара не могут быть пустыми.")
                while not (new_locations := list(input("Введите расположение товара, например C1, C2: ").split(', '))):
                    print("Расположение товара не может быть пустым.")

                new_item = {
                    "item_id": generate_unique_item_id(items),
                    "name": new_name,
                    "category": new_category,
                    "quantity": new_quantity,
                    "price": new_price,
                    "tags": new_tags,
                    "locations": new_locations
                }
                validate_new_item_data(items, new_item)
                add_item(items, new_item)
                save_items(items)
                print("Товар успешно добавлен.")
            except ValidationError as e:
                print(f"Ошибка добавления нового товара: {e}")

        elif choice == "2":
            item_id = input("Введите ID товара для удаления: ")
            if remove_item(items, item_id):
                save_items(items)
                print("Товар успешно удален.")
            else:
                print("Ошибка: товар с таким ID не найден.")

        elif choice == "3":
            while not (category := input("Введите категорию товара: ").lower()):
                print("Категория товара не может быть пустой.")

            while True:
                tags = set(input("Введите теги товара через запятую: ").lower().split(', '))
                if tags == {''}:
                    tags = {""}
                    break
            filtered_items = filter_items_by_category_and_tags(items, category, tags)
            if filtered_items:
                save_items_to_file(filtered_items, "filtered_items.json")
                print("Товары найдены, результаты сохранены в файл filtered_items.json:")
                for item in filtered_items:
                    print(item)
            else:
                print("Ошибка: не найдено товаров с указанной категорией и тегами.")

        elif choice == "4":
            location = input("Введите местоположение товара: ")
            found_items = find_items_by_location(items, location)
            if found_items:
                save_items_to_file(found_items, "items_at_location.json")
                print("Товары найдены, результат поиска сохранен в файл items_at_location.json:")
                for item in found_items:
                    print(item)
            else:
                print("Товары не найдены.")

        elif choice == "5":
            item_name = input("Введите наименование товара: ")
            if not item_name:
                return "Ошибка: наименование товара не указано."
            quantity = int(input("Введите новое количество товара: "))
            if quantity < 0:
                return "Ошибка: количество не может быть отрицательным."
            if update_item_quantity(items, item_name, quantity):
                save_items(items)
                print("Количество товара успешно обновлено.")
            else:
                print(f"Ошибка: товар с наименованием {item_name} не найден.")

        elif choice == "6":
            export_items_to_csv(items, "warehouse.csv")
            # print("Данные успешно экспортированы в warehouse.csv.")

        elif choice == "7":
            json_file = input("Введите имя файла для импорта: ")
            imported_items = import_items_from_json(json_file)
            if imported_items:
                items.extend(imported_items)
                save_items(items)
                print("Данные успешно импортированы.")
            else:
                print("Ошибка при импорте данных.")

        elif choice == "8":
            if generate_warehouse_report(items, "warehouse_report.txt"):
                print("Отчет сохранен в файл warehouse_report.txt.")
                with open("warehouse_report.txt", "r", encoding="utf-8") as report_file:
                    print(report_file.read())

        elif choice == "0":
            print("До свидания!")
            break

        else:
            print("Некорректный ввод. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
