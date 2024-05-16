# 6.27. Дано натуральное число n. Найти сумму

def find_number(n):
    sum_result = 0
    for i in range(0,n+1):
        sum_result += (n+i)**2
        return sum_result


def main():

    n = int(input("Введите натуральное число n"))
    find_number(n)



if __name__ == "__main__":
    main()