"""Bubble sort compares two adjacent elements and swaps them until they
are in the intended order
"""


# Bubble sort in Python

def BubbleSort(array):

    # loop to access each array element
    for i in range(len(array)):

        # loop to comapare array elements
        # change > to < to sort in descending order
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]

                # swapping elements if elements
                # are not in intended order.
                array[j] = array[j + 1]
                array[j + 1] = temp


data = [2, -9, 5, 56, 43, 3, 112]
print("Sorted Array in Ascending Order: ")
print(data)
