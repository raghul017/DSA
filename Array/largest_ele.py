arr = [1 ,2, 3, 4, 5, 6]

large_element = arr[0]   

for i in range(len(arr)):    
    if arr[i] > large_element:
        large_element = arr[i]

print(large_element)