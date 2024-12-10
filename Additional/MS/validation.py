# /project_order_management/CSV/validation.py

import datetime


class ValidationError(Exception):
    pass


def validate_order_data(order_data: dict, orders: list[dict]):
    for order in orders:
        if order['order_id'] == order_data['order_id']:
            raise ValidationError("ID заказа уже существует")

        if not (order['order_id'].strip()):
            raise ValidationError("ID отсутствует")


        if order['order_date'] > datetime.datetime.now():
            raise ValidationError("Дата указана не верно")

        if not order_data['customer_name']:
            raise ValidationError("Имя не может быть пустым")









