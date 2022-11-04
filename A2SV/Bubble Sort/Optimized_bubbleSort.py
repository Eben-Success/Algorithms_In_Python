"""Optimized bubble sort uses a variable called swapped to track sorted elements"""

def Optimized_bubbleSort(array):

    # loop through each element of array
    for i in range(len(array)):

        # keep track of swapping
        swapped = False

        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+ 1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp

                swapped = True
        if not swapped:
            break

data = [-2, 45, 0, 11, -9]
Optimized_bubbleSort(data)
print("Sorted Array in Asceding Order: ")
print(data)