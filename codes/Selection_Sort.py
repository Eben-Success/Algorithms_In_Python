"""
Insertion Sort Algorithm

1. Iterate from arr[i] to arr[N] over the array
2. Compare the current element (key) to its predecessor
3. If the key element is smaller than its predecessor, compare it to the elements before.
Move the greater elements one position up to make space for the swapped element.
"""


# Code Implementation

def insertion_sort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        last = i - 1
        while last >= 0 and key < arr[last]:
            arr[last + 1] = arr[last]
            last -= 1
        arr[last + 1] = key


# Driver code to test above
arr = [12, 11, 14, 4, 5]
insertion_sort(arr)
for i in range(len(arr)):
    print("% d" % arr[i])
