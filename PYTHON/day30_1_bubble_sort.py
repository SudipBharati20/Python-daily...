"""
=========================================
LESSON: BUBBLE SORT (COMPLETE GUIDE)
=========================================

DEFINITION:
Bubble Sort is a simple sorting algorithm that repeatedly compares
adjacent elements and swaps them if they are in the wrong order.

It is called "Bubble" because larger elements move (or bubble)
to the end of the list after each pass.

-----------------------------------------

HOW IT WORKS:
Example: [5, 1, 4, 2]

Pass 1:
5 > 1 → swap → [1, 5, 4, 2]
5 > 4 → swap → [1, 4, 5, 2]
5 > 2 → swap → [1, 4, 2, 5]

Pass 2:
1 < 4 → no swap
4 > 2 → swap → [1, 2, 4, 5]

Pass 3:
No swaps → list is sorted

-----------------------------------------

TIME COMPLEXITY:
Worst Case: O(n^2)
Best Case: O(n) (when optimized using a swap flag)

-----------------------------------------

KEY TERMS:
Pass: One complete iteration through the list
Swap: Exchange of two elements
Adjacent Elements: Elements next to each other

-----------------------------------------

ALGORITHM STEPS:
1. Start from the first element
2. Compare it with the next element
3. Swap if the first is greater
4. Continue till the end of the list
5. Repeat for n passes or until sorted

=========================================
"""

# FUNCTION: Bubble Sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


"""
=========================================
EXAMPLE
=========================================
"""

example = [5, 3, 8, 2]
print("Example Input:", example)
print("Sorted Output:", bubble_sort(example.copy()))


"""
=========================================
PROBLEM 1
=========================================

Question:
Sort the list in ascending order using Bubble Sort.

Input: [9, 7, 5, 3]

Expected Output: [3, 5, 7, 9]
"""

def problem1():
    arr = [9, 7, 5, 3]
    result = bubble_sort(arr)
    print("\nProblem 1 Solution:", result)

problem1()


"""
=========================================
PROBLEM 2
=========================================

Question:
Count the number of swaps required to sort the list.

Input: [4, 2, 1]

Expected Output:
Sorted list: [1, 2, 4]
Total swaps: 3
"""

def bubble_sort_with_swaps(arr):
    n = len(arr)
    swap_count = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # swap
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap_count += 1

    return arr, swap_count


def problem2():
    arr = [4, 2, 1]
    sorted_arr, swaps = bubble_sort_with_swaps(arr)

    print("\nProblem 2 Solution:")
    print("Sorted list:", sorted_arr)
    print("Total swaps:", swaps)

problem2()


