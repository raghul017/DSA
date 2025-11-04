def selection_sort(arr):
    n = len(arr)
    for i in range(0 , n-1):
        min_ele = i
        for j in range(i , n):
            if arr[j] < arr[min_ele]:
                min_ele = j
        
        temp = arr[i]
        arr[i] = arr[min_ele]
        arr[min_ele] = temp 
    return arr




arr = [40 , 19 , 36 , 20]
print(selection_sort(arr))