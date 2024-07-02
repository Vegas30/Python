# 7.1. Вывести на экран все целые числа от 100 до 200, кратные трем.

def numbers():
    for number in range(100, 201):
        if number % 3 == 0:
            print(number)

def main():

    numbers()

if __name__ == "__main__":
    main()
