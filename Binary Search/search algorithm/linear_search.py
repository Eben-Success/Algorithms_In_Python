def LinearSearch(arr, x):
    for i in range(0, len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [2, 5, 6, 7, 8, 5, 3]
x = 7

result = LinearSearch(arr, x)

if result == -1:
    print("Element not found in array")
else:
    print("Element found at ", result)
