# Insertion Sort

> Insertion sort is a sorting algorithm that places an unsorted element at its suitable place in each iteration.

# Selection Sort

>- Selection sort is a sorting algorithm that selects the smallest element in each iteration in an unsorted list and places it at the begining of the unsorted list until all the elements are sorted in the intended order.

### Time Complexity

### Time Complexity

|Time                         |Cases                     
|----------------|-----------------------------|
|Best Case| `O(n)`            |
|Worst Case         |`O(n^2)`                    
|Average Case         |`O(n^2)`|


Space Complexity: O(1) <br>
Stablity: Yes

## Time Complexities
### Worst Case Complexity O(n^2)
Suppose the array is in ascending order and you want to sort it in desceding order, in this case, the worst case occurs.
Each element has to be compared with each of the other elements so for every nth element, (n-1) number of comparisons are made.

### Best Case Complexity O(n)
When the array is already sorted, the outer loop runs for `n' number of times whiles the inner loop does not run at all.
So the best case occurs.

### Average Case Complexity: O(n^2)
It occurs when the elements of an array are in jumbled order (neither descending or ascending order)

### Space Complexity
Space complexity is `O(1)` because an extra variable `key` is used.

## Insertion Sort Application
* The array has small number of element.
* There are few elements left to be sorted.