def linear_search(list, target):
    """Return the index position of target if found, else returns None
    """

    for i in range(len(list)):
        if list[i] == target:
            return i
        return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")


numbers = [1, 2, 3, 4, 5, 6, 78, 9, 10]

result = linear_search(numbers, 78)

verify(result)
