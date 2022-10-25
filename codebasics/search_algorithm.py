from util import time_it


@time_it
def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1


@time_it
def binary_search(list, target):
    low, mid_index = 0, 0
    high = len(list) - 1

    while low <= high:
        mid_index = (low + high) // 2
        mid_number = list[mid_index]

        if mid_number == target:
            return mid_index

        if mid_number < target:
            low = mid_index + 1
        else:
            high = mid_index - 1
    return -1

@time_it
def binary_search_recursive(list, target, low, high):
    if high > low:
        return -1

    mid_index = 0
    mid_index = (low + high) // 2
    if mid_index < len(high) or mid_index < 0:
        return -1
    mid_number = list[mid_index]

    if mid_number == target:
        return mid_index

    if mid_number < target:
        low = mid_index + 1
    else:
        high = mid_index - 1

    return binary_search_recursive(list, target, low, high)



if __name__ == "__main__":
    # numbers_list = [12, 15, 17, 19, 21, 45, 67]
    # number_to_find = 12

    numbers = [i for i in range(1000001)]
    number_to_find = 1000000
    index = linear_search(numbers, number_to_find)
    print(f"Number found at index {index} using linear search")
    index = binary_search(numbers, number_to_find)
    print(f"Number found at index {index} using binary search")

    index = binary_search_recursive(numbers, number_to_find, 0, len(numbers))
