def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        mid = (first + last) // 2
        if list[mid] == target:
            return mid

        elif list[mid] < target:
            first = mid + 1

        else:
            last = mid - 1

    return None

# All the lines of code are constant time. However, as we keep redefining the mid,
# the length of the array keeps growing. And this result in the Logarithmic runtime.
