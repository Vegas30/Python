with open('example.txt', 'r', encoding='utf-8') as file:
    first_bytes = file.read(11)
    print(first_bytes)
