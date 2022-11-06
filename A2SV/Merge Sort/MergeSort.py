def mergeSort(array):
    if len(array) > 1:

        # m is the point where the array is divided into two subarrays.
        m = len(array) // 2

        L = array[:m]
        R = array[m:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        # Until we reach either end of L or M, pick the larger among
        # elements L and M and place them in the correct position at A[p..r]

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i+=1
            else:
                array[k] = R[j]
                j+=1
            k+=1

        while i < len(L):
            array[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            array[k] = R[j]
            j+=1
            k+=1



# Print the Array
def printList(array):
    for i in range(len(array)):
        print(array[i], end=' ')
    print()


# Driver program
if __name__ == '__main__':
    array = [45, -13, 2, 232, 1, 3, 6, 7, 8]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
