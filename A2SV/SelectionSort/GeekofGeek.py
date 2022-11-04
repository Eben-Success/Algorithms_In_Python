class Solution:

    def select(self, arr, i):
        min_idx = i

        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                min_idx = j

    def selectionsort(self, arr, n):
        for i in range(n-1):
            min_idx= self.select(arr, i)
            (arr[min_idx], arr[i]) = (arr[i], arr[min_idx])
