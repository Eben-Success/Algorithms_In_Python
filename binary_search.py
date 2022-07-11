# Return index of x in arr if present, else -1

def binary_search(arr, low, high, x):
    # Check base case
    if high >= low:
        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in the left subarry
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
