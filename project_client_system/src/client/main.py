# src/main.py
from clients import (filter_clients, extract_emails, group_by_tag, average_age_by_tag)
from report import transform_client_data, generate_report

clients = [
    {'name': 'Alice', 'age': 30, 'email': 'alice@example.com', 'tags': {'VIP', 'newsletter'}},
    {'name': 'Bob', 'age': 24, 'email': 'bob@example.com', 'tags': {'newsletter'}},
    {'name': 'Charlie', 'age': 35, 'tags': {'VIP', 'premium'}},
    {'name': 'David', 'age': 40, 'email': 'david@example.com', 'tags': {'premium'}},
    {'name': 'Eve', 'age': 29, 'email': 'eve@example.com', 'tags': {'newsletter', 'VIP'}}
]


def main():
    """
    Основная функция для запуска консольного приложения.
    ...

    :return:
    """
    while True:
        print("\nВыберите действие: ")
        print("1. Фильтрация клиентов.")
        print("2. Извлечение адресов эл.почты.")
        print("3. Группировка клиентов по тегам.")
        print("4. Рассчитать средний возраст по тегам.")
        print("5. Преобразование данных клиента.")
        print("6. Создать отчет о клиентах.")
        print("7. Выход.")

        choice = input("Введите номер: ")

        if choice == "1":
            try:
                min_age = int(input("Введите минимальный возраст клиента: "))
                tag = input("Введите тег: ")
                if tag.lower() == 'vip':
                    tag = tag.upper()
                filter_client = filter_clients(clients, min_age, tag)
                print(f"Отфильтрованный список клиентов по минимальному возрасту - {min_age}, с тегом - {tag}: ")
                print(*filter_client, sep="\n")
                print('\n'.join(filter_client))
                print(str(filter_client)[1:-1])
            except ValueError as e:
                print(f"Ошибка введённых данных - {e}")

        elif choice == "2":
            email_clients = extract_emails(clients)
            print("email's клиентов организации: ")
            print(*email_clients, sep='\n')

        elif choice == "3":
            group_tag = group_by_tag(clients)
            print("VIP: {VIP}\nPremium: {premium}\nNewsletter: {newsletter}".format(**group_tag))

        elif choice == "4":
            average_age = average_age_by_tag(clients)
            print("VIP: {VIP}\nPremium: {premium}\nNewsletter: {newsletter}".format(**average_age))

        elif choice == "5":
            trensform_data = transform_client_data(clients)
            print(f"Список кортежей (Имяб возраст): {trensform_data}")

        elif choice == "6":
            str_report = generate_report(clients)
            print(f"Отчет по клиентам:\n{str_report}")

        elif choice == "7":
            print("Выход")
            break
        else:
            print("Некорректный выбор действия")

if __name__ == '__main__':
    main()
