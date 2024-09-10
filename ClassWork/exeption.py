# 1.
def divide_1(num1: float, num2: float) -> float:
    """

    :param num1: Первое число (числитель)
    :param num2: Второе число (знаменатель)
    :return:
    """

    try:
        return num1 / num2
    except ZeroDivisionError as e:
        print("Errror: ", e)


# def get_integer_z2() -> int:
#     try:



def main():
    print(divide_1(num1=10, num2=0))


if __name__ == '__main__':
    main()
