# Merge Sort

Merge sort is a divide and conquer sorting algorithm. It recursiveley splits each portion of the origin array until it's comparing only two arrays with a single element each. It then merges the sorted subarrays back together.

Example :

```py
def merge_sort(arr):
    n = len(arr)

    if n > 1:
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        merge(left, right, arr)

    return arr

def merge(left, right, arr):

    i=  0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    if i == len(left):
        for item in right[j:]:
            arr[k] = item
            k += 1
    else:
        for item in left[i:]:
            arr[k] = item
            k += 1

```
Trace :

Unsorted List >> [8,4,23,42,16,15]
Sorted list >>[4, 8, 15, 16, 23, 42]

left | right | new list
-----|-------|---------
[4] | [23] | [4, 23]
[8] | [4, 23] | [4, 8, 23]
[16] | [15] | [15, 16]
[42] | [15, 16] | [15, 16, 42]
[4, 8, 23] | [15, 16, 42] | [4, 8, 15, 16, 23, 42]
