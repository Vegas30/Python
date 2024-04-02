# Дано двухзначное число. Найти:
# а) число единиц в нем;
# б) число десятков в нем;
# в) перевернуть;


number = int(input("Введите двузначное число: "))
tens = number // 10
digits = number % 10
new_number = digits * 10 + tens
print(f"Новое число: {new_number}")