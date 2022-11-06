# Merge Sort Algorithm

> It is a sorting algorithm that is based on the principle of Divide and Conquer.

MergeSort Algorithm

### Time Complexity


|Time                         | Cases      
|----------------|------------|
|Best Case| `O(nlogn)` |
|Worst Case         | `O(nlogn)` 
|Average Case         | `O(nlogn)` |


Space Complexity: O(n) <br>
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
