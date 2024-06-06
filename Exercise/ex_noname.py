# 4. Создайте список из чисел от 1 до 5. Расширьте его числовым рядом,
# где каждое последующее число является суммой предыдущих двух
# (например, Фибоначчи), пока длина списка не станет 10.
def dobav_element(arr):
    arr = arr.copy()
    for i in range(6,10+1):
        arr.append(i*i)
    return arr
def main():
    array = [1,2,3,4,5]
    arr = dobav_element(array)
    print(array, arr)
main()