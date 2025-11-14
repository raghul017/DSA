#pseudo code 
# repeat (numOfElements - 1) times
#   set the first unsorted element as the minimum
#   for each of the unsorted elements
#     if element < currentMinimum
#       set element as new minimum
#   swap minimum with first unsorted position



def selection_sort(arr):
    n = len(arr)
    for i in range(0 , n-1):
        min_ele = i
        for j in range(i , n):
            if arr[j] < arr[min_ele]:
                min_ele = j
        
        arr[i] , arr[min_ele] = arr[min_ele] , arr[i]
    return arr

arr = [40 , 19 , 36 , 20]
print(selection_sort(arr))