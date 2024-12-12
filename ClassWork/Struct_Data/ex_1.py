# Задача: Анализ списка транзакций
# Условие:
# У вас есть список транзакций. Каждая транзакция — это строка, которая описывает покупку в интернет-магазине, и имеет следующий формат:
#
# "<id покупателя> <товар> <количество> <цена>"
# Необходимо выполнить следующие шаги:
#
# Подсчитать общую сумму покупок для каждого покупателя.
# Найти наиболее покупаемый товар.
# Найти покупателя, который потратил больше всех.
# Найти топ-3 товаров по общей стоимости покупок.
# Для каждого покупателя вывести список товаров, которые он купил (с учетом количества).
# Для каждого товара вывести список покупателей, которые его покупали, с количеством купленных единиц.
#
# Входные данные:
# Список строк, где каждая строка — это транзакция:
#
# transactions = [
#     "1 iPhone 2 999.99",
#     "2 MacBook 1 1299.99",
#     "1 iPhone 1 999.99",
#     "3 AirPods 3 199.99",
#     "2 MacBook 2 1299.99",
#     "3 AirPods 1 199.99",
#     "1 iPhone 1 999.99",
#     "3 MacBook 1 1299.99",
#     "2 AirPods 1 199.99",
#     "3 iPhone 1 999.99"
# ]

import collections as coll
transactions = [
    "1 iPhone 2 999.99",
    "2 MacBook 1 1299.99",
    "1 iPhone 1 999.99",
    "3 AirPods 3 199.99",
    "2 MacBook 2 1299.99",
    "3 AirPods 1 199.99",
    "1 iPhone 1 999.99",
    "3 MacBook 1 1299.99",
    "2 AirPods 1 199.99",
    "3 iPhone 1 999.99"
]

total_sum_client = coll.defaultdict(float)
for transaction in transactions:
    id_client, _, quantity, price = transaction.split()
    quantity = int(quantity)
    price = float(price)
    total_sum_client[id_client] += quantity * price #round?

print(dict(total_sum_client))

product_popular = coll.Counter()
print(product_popular)
for transaction in transactions:
    _, product, quantity, _ = transaction.split()
    quantity = int(quantity)
    product_popular[product] += quantity

popular = product_popular.most_common(1) #? распаковка
print(f"Популярный товар - {popular[0][0]} в количестве {popular[0][1]}")


max_client = max(total_sum_client, key=total_sum_client.get)
print(max_client)

popular = product_popular.most_common(3)
print(popular)

product_id = coll.defaultdict(list)
for transaction in transactions:
    id_client, product, quantity, _ = transaction.split()
    quantity = int(quantity)
    product_id[id_client].append((product, quantity))

print(dict(product_id))

list_line = coll.defaultdict(list)
for transaction in transactions:
    id_client, product, quantity, _ = transaction.split()
    quantity = int(quantity)
    list_line[product].append((id_client, quantity))

print(list_line)