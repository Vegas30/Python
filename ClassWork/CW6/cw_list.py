list2 = [1, 2, 3]
print(type(list2))

list1 = [1, 23, 4, 5]

number = reversed(list1)
number2 = list1.reverse()  # это неверная запись reverse() ни чего не возвращает
list1.reverse()  # вот так правильно
print(list(number))
print(number2)  # Будет None
print(list1)

list3 = [1, 2, 3, 4, 5]
list3.reverse()
print(list3)

list3.append(int(input("Введите число: ")))
print(list3)

