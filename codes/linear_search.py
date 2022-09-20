def linear_search(input_list: list, element: int):
    """This algorithm searches through the input_list and prints the index of the
    given element."""

    list_len = len(input_list)
    for i in range(list_len):
        if input_list[i] == element:
            return i

    return -1


myList = [2, 3, 4, 5, 5, 76, 4, 3, 4, 6, 3, 4, 3, 44]
print("Given list is:  ", myList)
element = 44
position = linear_search(myList, element)
print(f"Element {element} is at postion: ", position)
