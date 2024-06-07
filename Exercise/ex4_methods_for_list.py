

# 4. Создайте список из чисел от 1 до 5. Расширьте его числовым рядом,
# где каждое последующее число является суммой предыдущих двух
# (например, Фибоначчи), пока длина списка не станет 10.
def dobav_element(array):
    while len(array) < 10:
        array.append(array[-1] + array[-2])

def main():
    array = [1,2,3,4,5,9]
    dobav_element(array)
    print(array)
main()