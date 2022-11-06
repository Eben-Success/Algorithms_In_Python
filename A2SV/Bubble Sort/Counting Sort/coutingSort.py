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


