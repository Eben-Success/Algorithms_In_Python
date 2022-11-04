"""Selection sort selects the smallest element in an unsorted array
in each iteration and places it at the begining of the unosrted list"""

def selectionSort(array, size):

    for step in range(size):
        min_idx = step

        for i in range(step+1, size):

            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop

            if array[i] < array[min_idx]:
                min_idx = i

        # swap the two elements
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print("Sorted Array in Ascending order ")
print(data)