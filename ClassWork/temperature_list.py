import random


def average(array):
    return sum(array) / len(array)


def pop_array(array, index):
    array_copy = array[:]
    return array_copy.pop(index)


def print_menu():
    print("\nМеню: ")
    print("")


def index_day(month, n):
    for day in month:
        if day > n:
            result = month.index(day)
        return result


def main():
    main_array = temperature_array = [random.randint(-5, 5) for _ in range(30)]
    print(temperature_array)
    n=4
    result_1 = [temperature_array.index(x) for x in temperature_array if x > n]
    print(result_1)



if __name__ == '__main__':
    main()
