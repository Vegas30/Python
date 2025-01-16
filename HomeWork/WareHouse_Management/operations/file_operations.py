# WareHouse_Management/operations/file_operations.py
import json

"""Модуль для работы с файлами"""


def save_items_to_file(items: list[dict], file_path: str):
    """Функция сохраняет список товаров в файл JSON"""
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(items, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Ошибка при сохранении в файл: {e}")


def load_items_from_file(file_path: str) -> list[dict]:
    """Функция загружает список товаров из файла JSON"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл не найден. Создайте новый список товаров.")
        return []
    except json.JSONDecodeError:
        print("Ошибка чтения файла: некорректный формат JSON.")
        return []

# def save_items_to_file(items: list[dict], file_path: str):
#     """Функция сохраняет список товаров в файл JSON"""
#     try:
#         # Преобразуем множества в списки перед сохранением
#         json_ready_items = [
#             {**item, 'tags': list(item['tags'])} for item in items
#         ]
#         with open(file_path, 'w', encoding='utf-8') as f:
#             json.dump(json_ready_items, f, ensure_ascii=False, indent=4)
#     except Exception as e:
#         print(f"Ошибка при сохранении в файл: {e}")

# def load_items_from_file(file_path) -> list[dict]:
#     """Функция загружает список товаров из файла JSON"""
#     try:
#         with open(file_path, 'r', encoding='utf-8') as f:
#             items = json.load(f)
#             # Преобразуем списки обратно в множества
#             for item in items:
#                 item['tags'] = set(item['tags'])
#             return items
#     except FileNotFoundError:
#         print("Файл не найден. Создайте новый список товаров.")
#         return []
#     except json.JSONDecodeError:
#         print("Ошибка чтения файла: некорректный формат JSON.")
#         return []
