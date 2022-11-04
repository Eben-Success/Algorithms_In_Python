"""Selection sort selects the smallest element in an unsorted array
in each iteration and places it at the begining of the unosrted list"""

def selectionSort(array, size):

    for step in range(size):
        min_idx = step

        for i in range(step+1, size):

            # to sort in descending order,