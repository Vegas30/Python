def first_function():
    second_function()


def second_function():
    third_function()


def third_function():
    print("Call Stack demonstration")


first_function()