# Create a binary search on my own

def binary_search(arr, x):
    """Create a function for binary search"""
    low = 0
    mid = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # if x is smaller, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # if x is larger, ignore the right half
        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1



arr = [2,4,5,56,6,4,5]
x = 5

ok = binary_search(arr, x)
print(ok)
