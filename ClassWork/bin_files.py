# 1. Программа должна записать строку в бинарный файл и сохранить длину
# закодированного текста для правильного декодирования при чтении.

text = "Привет! Я буду а потом не буду."

encoded_text = text.encode('utf-8')
length = len(encoded_text)
print(encoded_text)
print(length)

with open('length_encoded.bin', 'wb') as file:
    file.write(encoded_text)
    file.write(length.to_bytes(2, byteorder='little'))

with open('length_encoded.bin', 'rb') as file:
    file.seek(-2, 2)
    length_data = file.read(2)
    length = int.from_bytes(length_data, byteorder='little')

    file.seek(0)
    encoded_text = file.read(length)
decoded_text = encoded_text.decode('utf-8')
print(decoded_text, length)

# 2. Программа должна закодировать список строк,
# записать их в бинарный файл, а затем считать и декодировать обратно в список

lines = ['first line', 'вторая строка', 'вторая stroka']
with open('length_encoded.bin', 'wb') as file:
    for line in lines:
        line = line + '\n'
        encoded_text = line.encode('utf-8')
        file.write(encoded_text)

decoded_list = []
with open('length_encoded.bin', 'rb') as file:
    for bline in file.readlines():
        decoded_text = bline.decode('utf-8')
        decoded_text = decoded_text.strip()
        decoded_list.append(decoded_text)
print(decoded_list)

# 3. Программа, которая читает список клиенов из текстового файла
# и сериализует его в формат JSON, а затем записывает результат в файл clients.json
# {
#     "clients": [
#         {'name': "Иван"}
#     ]
# }

import json

def read_client_to_file(filename: str) -> list[dict]:
    clients = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            name_client, info_client = line.strip().split(": ") #['Иван', '34, Москва']
            age, city = info_client.split(', ') #['34', 'Москва']
            client = {
                'name': name_client,
                'age': int(age),
                'city': city
            }
            clients.append(client)
    return clients


def write_client_to_json(clients: list[dict], json_filename: str) -> None:
    data = {'clients': clients}
    with open(json_filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def load_clients_to_json(json_filename: str) -> None:
    with open(json_filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    print(data)

def main():
    input_filename = 'client.txt'
    output_filename = 'client.json'
    client_data = read_client_to_file(input_filename)
    write_client_to_json(client_data, output_filename)
    print(f"Данные успешно сериализованы в файл {output_filename}")
    load_clients_to_json(output_filename)

main()
