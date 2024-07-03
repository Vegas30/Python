import random


def func(arr):
    filtered_array = list(filter(lambda x: x % 2 == 0, arr))
    print(filtered_array)
    filtered_array.sort(reverse=True)
    print(filtered_array)
    array_multi_2 = list(map(lambda x: x * 2, arr))
    print(array_multi_2)
    only_five_array = array_multi_2[:5]
    print(only_five_array)
    result = lambda x: all(i > 10 for i in x)
    print(result(only_five_array))
def main():
    array = [random.randint(-100, 100) for _ in range(20)]
    print(array)

    array_copy = array.copy()
    func(array_copy)


if __name__ == '__main__':
    main()
