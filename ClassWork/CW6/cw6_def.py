from random import randint


def empty_func():
    pass


def summ_numbers(num1, num2):
    print(num1 + num2)


a = randint(-5, 5)
b = randint(10, 15)

summ_numbers(a, b)


def names(surname="Фамилия", name="Максим", age=13):
    print(surname, name, age)


names(surname="Макаров", age="Максим", name=13)


def summ_num2(a, b=5):
    result = a + b
    result2 = a - b
    return result, result2


res_new = summ_num2(2)
result1, result2 = summ_num2()
print(res_new)
