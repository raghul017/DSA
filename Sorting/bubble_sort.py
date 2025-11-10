def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        did_swap = 0
        for j in range(0 , n-i-1):
            if arr[j] > arr[j+1]:
                arr[ j ] , arr[j + 1 ] = arr[j + 1] , arr[j]
                did_swap = 1
        if did_swap == 0:
            break
        
    return arr

print(bubble_sort([7,4,1,5,3]))
print(bubble_sort([1,2,3,4,5]))