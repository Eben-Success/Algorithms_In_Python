def mergeSort(array):
    if len(array) > 1:

    # m is the point where the array is divided into to subarrays

    m = len(array) / 2
    left_array = array[:m]
    right_array = array[m:]

    # Sort the two halves
    mergeSort(left_array)
    mergeSort(right_array)

    i = j = k = 0

    # Until we reach the end of either left_array or right_array, pick the larger among
    # elements left_array and right_array and place them in the correct position at A[p...r]

