"""Selection sort selects the smallest element in an unsorted list
in each iteration and places that element at the beginining of the unsorted list.
"""

def selectionSort(array, size):

    for step in range(size):
        min_idx = step

        for i in range(step+1, size)
