# Bubble Sort

>- Bubble sort is an algorithm that compares two adjacent elements and swaps them until they're in the intended order.

### Time Complexity

### Time Complexity

|Time                         |Cases                     
|----------------|-----------------------------|
|Best Case| `O(n)`            |
|Worst Case         |`O(n^2)`                    
|Average Case         |`O(n^2)`|

### Space Complexity
Space Complexity of Bubble Sort: O(1)
* Because an extra variable is used for swapping.

Space complexity of optimized bubble sort: O(2)


Stablity: Yes

## Opitized Bubble Sort

We can introudce an extra variable `swapped`. The
value of `swapped` is set to true if there occurs swapping of elements. Otherwise, it is set **false**.
After an iteraction, if there is no swapping, the value of `swapped` will be **false**.
This means elements are already sorted and there's no need to perform further iterations.