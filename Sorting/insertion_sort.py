def insertion_sort(arr):
    n = len(arr)
    for i in range(0 , n):
        j = i 
        while((j > 0) and (arr[j-1] > arr[j])):
            arr[j - 1] , arr[j] = arr[j] , arr[j - 1]
            j -=1
    
    return arr

print(insertion_sort([2,45,12,15,3]))
print(insertion_sort([45,2,32,12,5,3]))