# Blog for Code Challenge 26 - Insertion Sort

Description

Selection Sort is a sorting algorithm in the same family as bubble sort and selection sort but simpler and more efficient. Selection sort works by iterating across the array starting at the front and comparing if the value of the element next to it is lower. If the next door value is lower the elements change places.

Pseudocode

```py
SelectionSort(int[] arr)
    DECLARE n <-- arr.Length;
    FOR i = 0; i to n - 1
        DECLARE min <-- i;
        FOR j = i + 1 to n
            if (arr[j] < arr[min])
                min <-- j;

        DECLARE temp <-- arr[min];
        arr[min] <-- arr[i];
        arr[i] <-- temp;
```

Trace :

Sample Array: [8,4,23,42,16,15]

### Pass 1:
when i=1

![pass1](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-26/solutions/assets/selectionSort1.png)

In the first pass through of the selection sort, we evaluate if there is a smaller number in the array than what is currently present in index 0. We find this smaller number right away in index 1. The minimum value gets updated to remember this index. At the end of the evaluation, the smaller number will be swapped with the current value in index i. This results in our smallest number of our array being placed first.

### Pass 2:
when i=2
![pass1](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-26/solutions/assets/selectionSort2.png)

The second pass through the array evaluates the remaining values in the array to see if there is a smaller value other than the current position of i. 8 is the 2nd smallest number in the array, so it “swaps” with itself. The minimum value does not change at all during the iteration of this pass.

### Pass 3:
when i=3
[4,8,23,42,16,15]

![pass1](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-26/solutions/assets/selectionSort3.png)

The third pass through evaluates the remaining indexes in the array, starting at position 2. Both position 4 and 5 are smaller than the value in position 2. Each time a smaller number than the current minimum is found, the variable will update to the new smallest number. In this case, 15 is the next smallest number. As a result, it will swap with position 2.


### Pass 4:
when i=4
![pass1](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-26/solutions/assets/selectionSort4.png)

The 4th pass through on the array proves that 16 is the next smallest number in the array, and as a result, switches places with the 42.

### Pass 5:
when i=5
![pass1](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-26/solutions/assets/selectionSort5.png)

The 5th pass through of the array only has one other index to evaluate. Since the last index value is larger than index 4, the two values will swap.


### Pass 6:

![pass1](https://codefellows.github.io/common_curriculum/data_structures_and_algorithms/Code_401/class-26/solutions/assets/selectionSortFinal.png)

On its final iteratation through the array, it will swap places with itself as it evaluates the value against itself.

After this iteration, i will increment to 6, forcing it to break out of the outer for loop and leaving our array now sorted.


i | j | temp | list
--|---|------|-----
1 | -1 | 4 | [4, 8, 23, 42, 16, 15]
2 | 1 | 23 | [4, 8, 23, 42, 16, 15]
3 | 2 | 42 | [4, 8, 23, 42, 16, 15]
4 | 1 | 16 | [4, 8, 16, 23, 42, 15]
5 | 1 | 15 | [4, 8, 15, 16, 23, 42]

Sorted list: `[4, 8, 15, 16, 23, 42]`

Efficency:

- Time: O(n^2)
- Space: O(1)
