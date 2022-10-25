"""
Find index of all the occurances of a number from sorted list

numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
number_to_find = 15
This should return 5,6,7 as indices containing number 15 in the array
"""

def binary_search(list, target):
    low, mid_index = 0,0
    high = len(list) - 1

    while low <= high:
        mid_index = (low + high ) // 2
        mid_number = list[mid_index]

        if mid_number == target:
            return mid_index

        if mid_number < target:
            low = mid_index + 1
        else:
            high = mid_index - 1

    return -1


def find_all_occurances(list, target):
    index = binary_search(list, target)
    indices = [index]