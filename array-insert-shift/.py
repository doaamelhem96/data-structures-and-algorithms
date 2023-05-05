def insertShiftArray(arr, value):
    n = len(arr)
    mid = n // 2
    
    for i in range(n - 1, mid, -1):
        arr[i] = arr[i - 1]
    
    arr[mid] = value
    
    return arr
arr = [1, 2, 4, 5]
value = 3
new_arr = insertShiftArray(arr, value)
print(new_arr)
