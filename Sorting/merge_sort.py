def merge_sort(arr):
    # Base case: if the list has 0 or 1 element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Find the middle index to split the list
    mid = len(arr) // 2

    # Split the list into two halves
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    # This will store the merged sorted list
    result = []

    i = 0  # pointer for left list
    j = 0  # pointer for right list

    # Compare elements from both lists and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add any leftover elements from the left list
    while i < len(left):
        result.append(left[i])
        i += 1

    # Add any leftover elements from the right list
    while j < len(right):
        result.append(right[j])
        j += 1

    # Return the fully merged and sorted list
    return result


# Test the function
print(merge_sort([3, 2, 4, 1, 3]))