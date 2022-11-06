def mergeSort(array):
    if len(array) > 1:

        m = len(array) // 2

        L = array[:m]
        R = array[m:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

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