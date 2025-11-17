#for largest and also second largest 

arr = [1 ,2, 3, 4, 5, 6]

large_element = arr[0]   

for i in range(len(arr)):    
    if arr[i] > large_element:
        large_element = arr[i]

second_largest = 0

for i in range(len(arr)):
    if (arr[i] > second_largest and arr[i] != large_element):
        second_largest = arr[i]

print(second_largest)


#Second largest optimized solution
arr = [1,2,3,4,5,6]

largest = arr[0]
second_largest = float('-inf')

for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i

print(second_largest)