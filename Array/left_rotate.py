def left_rotate(arr , k):
    n= len(arr)

    for i in range(k):
        temp = arr[0]
        for j in range(n ,1):
            arr[j-1] = arr[j]

        arr[1] = temp
    return arr
arr = [1,2,3,4,5,6,7]
print(left_rotate(arr , 3))