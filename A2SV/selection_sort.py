"""Selection sort selects the smallest element in an unsorted list
in each iteration and places that element at the beginining of the unsorted list.
"""


def selectionSort(array, size):
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop

            if array[i] < array[min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print("Sorted Array in Asceding Order: ")
print(data)
