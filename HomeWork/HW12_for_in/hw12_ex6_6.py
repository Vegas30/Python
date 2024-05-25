# 6.6. Одна штука некоторого товара стоит 20,4 руб. Напечатать
# таблицу стоимости 2, 3, ..., 20 штук этого товара.

def print_price_table(price_per_unit, max_quantity):
    for quantity in range(2, max_quantity + 1):
        total_price = price_per_unit * quantity
        print(f"{quantity} шт. - {total_price:.2f} руб.")


def main():
    price_per_unit = 20.4
    max_quantity = 20
    print_price_table(price_per_unit, max_quantity)


if __name__ == "__main__":
    main()
