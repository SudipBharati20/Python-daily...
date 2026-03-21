"""
========================================
        BUBBLE SORT PROJECT
========================================

1. DEFINITION:
Bubble Sort is a simple sorting algorithm that repeatedly compares
adjacent elements and swaps them if they are in the wrong order.

2. HOW IT WORKS:
- Start from the first element
- Compare it with the next element
- Swap if needed
- Move forward
- Repeat the process until the list is sorted

3. WHY CALLED "BUBBLE" SORT:
Because the largest elements "bubble up" to the end of the list
after each pass.

4. TIME COMPLEXITY:
Best Case: O(n)       (already sorted)
Worst Case: O(n^2)    (reverse order)

5. SPACE COMPLEXITY:
O(1) → No extra memory needed

========================================
        BASIC BUBBLE SORT FUNCTION
========================================
"""

def bubble_sort(arr):
    n = len(arr)
    
    # Traverse through all elements
    for i in range(n):
        
        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            
            # Swap if current element is greater than next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


"""
========================================
        EXAMPLE
========================================
"""

example = [5, 2, 9, 1, 5, 6]
print("Original List:", example)
print("Sorted List:", bubble_sort(example))


"""
========================================
        IMPROVED VERSION
(Stops early if already sorted)
========================================
"""

def optimized_bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps happened, list is sorted
        if not swapped:
            break
    
    return arr


"""
========================================
        PROBLEM 1
Sort numbers entered by the user
========================================
"""

def user_sort():
    n = int(input("How many numbers? "))
    numbers = []
    
    for i in range(n):
        num = int(input("Enter number: "))
        numbers.append(num)
    
    print("Before sorting:", numbers)
    print("After sorting:", bubble_sort(numbers))


"""
========================================
        PROBLEM 2
Sort list in descending order
========================================
"""

def bubble_sort_desc(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            
            # Change sign for descending
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# Test Problem 2
test = [3, 7, 1, 9, 2]
print("Descending Order:", bubble_sort_desc(test))


"""
========================================
        EXTRA PRACTICE QUESTIONS
========================================

Q1: Modify bubble sort to count number of swaps.
Q2: Sort a list of strings alphabetically.
Q3: Find the largest number using only bubble sort logic.

========================================
        END OF PROJECT
========================================
"""