# WareHouse_Management/operations/validation.py

class ValidationError(Exception):
    pass

def validate_new_item_data(items: list[dict], new_item: dict):
    if not new_item['item_id'].strip():
        raise ValidationError("Введите ID товара.")

    for item in items:
        if item['item_id'] == new_item['item_id']:
            raise ValidationError("ID товара уже существует.")

    if not new_item['name'].strip():
        raise ValidationError("Введите наименование товара.")

    if not new_item['category'].strip():
        raise ValidationError("Введите категорию товара.")

    # if not isinstance(new_item['category'], str):
    #     raise ValidationError("Ошибка: 'category' должна быть строкой.")

    if not isinstance(new_item['quantity'], int) or new_item['quantity'] < 0:
        raise ValidationError("'quantity' должно быть неотрицательным целым числом.")

    if not isinstance(new_item['price'], (int, float)) or new_item["price"] < 0:
        raise ValidationError("'price' должен быть неотрицательным числом.")

    if not new_item['tags']:
        raise ValidationError("Укажите хотя бы один 'tag'.")

    if not new_item['locations']:
        raise ValidationError("Обязательно укажите 'locations'.")
