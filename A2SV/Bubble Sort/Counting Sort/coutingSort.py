def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each elements in count array
    for i in range(0, size):
        count[array[i]] += 1

    # store the cumulative count
    for i in range(1, 10):
        count[i] += count[i-1]

    # Find the index of each element of the original array in count array
    # place the elements in output array

    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copy the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]

data = [4, 5, 2, 6, 2, 6, 7, 3, 23 ,-23, 23]
countingSort(data)
print("Sorted Array in Ascending order: ")
print(data)
