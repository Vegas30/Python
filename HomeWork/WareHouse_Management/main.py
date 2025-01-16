# WareHouse_Management/main.py
from operations.file_operations import load_items_from_file, save_items_to_file
from operations.ware_operations import add_item, remove_item, find_items_by_location, filter_items_by_category_and_tags, \
    update_item_quantity
from operations.validation import validate_new_item_data, ValidationError
import csv
import json

FILE_PATH = "data/warehouse.json"


def load_items():
    """Вызываем функцию для загрузки товаров из файла JSON"""
    return load_items_from_file(FILE_PATH) or []

def save_items(items):
    """Вызываем функцию для сохранения товаров в файл JSON"""
    save_items_to_file(items, FILE_PATH)

def export_items_to_csv(items, csv_file):
    try:
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['name', 'category', 'quantity', 'price', 'tags', 'locations'])
            for item in items:
                writer.writerow([
                    item['name'],
                    item['category'],
                    item['quantity'],
                    item['price'],
                    ','.join(item['tags']),
                    ' '.join(item['locations'])
                ])
        return "Данные успешно экспортированы в operations."
    except Exception as e:
        return f"Ошибка при экспорте в operations: {e}"


def import_items_from_json(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            items = json.load(f)
            for item in items:
                if not all(key in item for key in ['name', 'category', 'quantity', 'price', 'tags', 'locations']):
                    raise ValueError("Некорректная структура данных.")
            return items
    except FileNotFoundError:
        return "Ошибка: файл не найден."
    except json.JSONDecodeError:
        return "Ошибка: некорректный формат JSON."
    except ValueError as e:
        return f"Ошибка: {e}"


def generate_warehouse_report(items, report_file):
    try:
        with open(report_file, 'w', encoding='utf-8') as f:
            for item in items:
                if not item['locations']:
                    raise ValueError(f"У товара '{item['name']}' отсутствуют местоположения.")
                f.write(
                    f"Товар: {item['name']}, Количество: {item['quantity']}, Местоположения: {', '.join(item['locations'])}\n")
        return "Отчет успешно создан."
    except Exception as e:
        return f"Ошибка при создании отчета: {e}"


def main():
    """Консольное приложение для управления складом товаров."""

    items = load_items()

    new_item = {
        "item_id": "1",
        "name": "Table",
        "category": "Furniture",
        "quantity": 8,
        "price": 150.50,
        "tags": ["office", "sale"],
        "locations": ["C1", "C2"]
    }

    print(add_item(items, new_item, FILE_PATH))
    print(remove_item(items, "Chair", FILE_PATH))
    print(filter_items_by_category_and_tags(items, "Furniture", ["sale"], "filtered_items.json"))
    print(find_items_by_location(items, "A1", "items_at_location.json"))
    print(update_item_quantity(items, "Laptop", 12, FILE_PATH))
    print(export_items_to_csv(items, "warehouse.csv"))
    print(import_items_from_json("import_data.json"))
    print(generate_warehouse_report(items, "warehouse_report.txt"))

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

        choice = input("Введите номер действия: ")
        if choice == "1":
            try:
                new_item = {
                    "item_id": input("Введите номер товара: "),
                    "name": input("Введите наименование товара, например Table: "),
                    "category": input("Введите категорию товара, например Furniture: "),
                    "quantity": int(input("Введите количество товара в виде целого числа, например 8: ")),
                    "price": round(float(input("Введите цену товара, например 150.50: ")), 2),
                    "tags": list(set(str(input("Введите метки товара (tags) через запятую, например office, sale: ").split(', ')))),
                    "locations": list(input("Введите расположение товара, например C1, C2: ").split(', '))
                }
                validate_new_item_data(items, new_item)
                add_item(items, new_item, FILE_PATH)
                save_items(items)
                print("Товар успешно добавлен.")
            except ValidationError as e:
                print(f"Ошибка добавления нового товара: {e}")

        elif choice == "2":
            item_id = input("Введите ID товара для удаления: ")
            remove_item(items, item_id, FILE_PATH)

        elif choice == "3":
            category = input("Введите категорию товара: ")
            tags = list(set(input("Введите теги товара через запятую: ").split(', ')))
            filter_items_by_category_and_tags(items, category, tags, "filtered_items.json")

        elif choice == "4":
            location = input("Введите местоположение товара: ")
            find_items_by_location(items, location, "items_at_location.json")

        elif choice == "5":
            item_name = input("Введите наименование товара: ")
            quantity = int(input("Введите новое количество товара: "))
            update_item_quantity(items, item_name, quantity, FILE_PATH)

        elif choice == "6":
            export_items_to_csv(items, "warehouse.csv")

        elif choice == "7":
            json_file = input("Введите имя файла для импорта: ")
            import_items_from_json(json_file)

        elif choice == "8":
            generate_warehouse_report(items, "warehouse_report.txt")

        else:
            print("Некорректный ввод. Попробуйте еще раз.")



# Пример использования
if __name__ == "__main__":
    main()
