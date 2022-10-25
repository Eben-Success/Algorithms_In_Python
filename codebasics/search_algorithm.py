def linear_search(numbers_list, number_to_find):
    for index, element in enumerate(numbers_list):
        if element == number_to_find:
            return index
    return -1


def binary_search(numbers_list, number_to_find):
    low = 0
    high = len(numbers_list) - 1
    mid_index = 0

    while low <= high:
        mid_index = (low + high) // 2
        mid = numbers_list[mid_index]

        if mid == number_to_find:
            return mid
        elif mid < number_to_find:
            low = mid + 1
        else:
            high = mid - 1
    return -1



if __name__  == "__main__":
    numbers_list = [12,15,17,19,21,45,67]
    number_to_find = 45

    index = linear_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using linear search")
    index = binary_search(numbers_list, number_to_find)
    print(f"Number found at index {index} using binary search")