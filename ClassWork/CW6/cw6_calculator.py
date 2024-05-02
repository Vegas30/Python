def calc(a, b, mat_oper="+"):
    if mat_oper != "+":
        if mat_oper == "-":
            res = a - b

        elif mat_oper == "/":
            if b == 0:
                print("Деление на ноль")
            else:
                res = a / b

        elif mat_oper == "*":
            res = a * b

    else:
        res = a + b

    return res

с = input("Введите оператор: ")
result = calc(1, 2, с)
print(result)

