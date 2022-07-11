# Python 3 program for recursive binary search

# Return index of x in arr if present, else -1
def binary_search(arr, low, high, x):

    #
    if high >= low:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        return -1
