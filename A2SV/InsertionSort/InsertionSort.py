"""
Insertion sort is a sorting algorithm that places an unsorted element at its suitable place
in each iteration.
"""

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1

        # compare key with each element on the left of it until an
        # element smaller than it is found.

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1

        # Place key after the element just smaller than it
        array[j+1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print("Sorted Array in Ascending Order: ")
print(data)
