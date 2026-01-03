arr = [1, 2, 3, 4, 5]

# Accessing elements in an array
# Time complexity: O(1) as it accesses the elements using index
print(arr[0])
print(arr[3])

# To find the length of the array - use len()
print(len(arr))

# Traversal - look into each element of the array either to find some number or perform some operations
# Time complexity is O(n) - as we traverse into all the elements in the array where n is the size of the array

# Method 1
for val in arr:
    print(val)

# Method 2
for i in range(len(arr)):
    print(arr[i])

# List comprehension for traversal/operations (e.g., double values)
doubled = [val * 2 for val in arr]
print(doubled)  # [2, 4, 6, 8, 10]

# Search

# Linear search - works on unsorted list
# Time complexity: O(n)
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Found at index i
    return -1  # Not found

print(linear_search(arr, 3))  # Output: 2

# Binary search - works only on SORTED list
# Time complexity: O(log n) - divides search space in half each time
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

# Example usage (arr must be sorted)
sorted_arr = [1, 2, 3, 4, 5, 10, 20, 30]
print(binary_search(sorted_arr, 10))  # Output: 5
print(binary_search(sorted_arr, 7))   # Output: -1

# Built-in alternative: bisect module (more efficient and handles edge cases)
import bisect
print(bisect.bisect_left(sorted_arr, 10))  # Returns insertion point (or index if exists)

# Insertion: inserting value in the array. In Python, array (list) is dynamic so the array shrinks/expands automatically
# Best/average case: O(1) - insertion at the end
arr.append(40)

# Worst case/edge case: O(n) - insert at beginning or in the middle requires shifting elements
arr.insert(1, 5)

# Manual shift
def insert(arr, index, value):
    arr.append(None)
    for i in range(len(arr) - 2, index - 1, -1):
        arr[i + 1] = arr[i]
    arr[index] = value
    return arr

# Alternative: Using slicing (creates new list)
def insert_2(arr, index, value):
    return arr[:index] + [value] + arr[index:]

# Note: These calls modify/print the current state of 'arr' - for clean testing, reset 'arr' if needed
print(insert(arr, 2, 5))
print(insert_2(arr, 5, 10))

# Deletion: deleting an element from an array at a specific position
# Best case: O(1) for the end (pop last)

# Manual
def delete(arr, index):
    if index < 0 or index >= len(arr):
        return arr
    for i in range(index, len(arr) - 1):
        arr[i] = arr[i + 1]
    arr.pop()
    return arr

print(delete(arr, 2))

# Built-in methods
# arr.pop()  # Delete last element
# arr.pop(2)  # Delete element at given index and shifts other elements
# arr.remove(10)  # Remove the element by value (first occurrence)
# arr.clear()  # Clear all values in the arr

# Updation - update the old value to new value at the desired index
# Time complexity: O(1)
arr[1] = 2

# Copying - To avoid mutating original (lists are mutable)
import copy
arr_copy = copy.copy(arr)  # Shallow copy, O(n)
# Or: arr_copy = arr[:]  # Slicing copy

# Sorting
arr.sort()  # In-place sort, O(n log n)
sorted_arr = sorted(arr)  # Returns new sorted list, O(n log n)

# Summary Table
"""
| Operation              | Time         |
| ---------------------- | ------------ |
| Access                 | O(1)         |
| Search (linear)        | O(n)         |
| Search (binary, sorted)| O(log n)     |
| Insert middle          | O(n)         |
| Delete middle          | O(n)         |
| Update                 | O(1)         |
| Sort                   | O(n log n)   |
"""
