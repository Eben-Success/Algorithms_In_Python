# Linear Search in Python

def Linear_search(array, x, array_size):
    array_size = len(array)

    for i in array:
        if array[i] == x:
            return i
        else:
            return -1


array = [2, 3, 4, 5, 6, 7, 4]
x = 4
