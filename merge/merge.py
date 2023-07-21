def mergesort(arr):
    if len(arr) > 1:
        n = len(arr)
        mid = n // 2
        left = arr[:mid]
        right = arr[mid:]
        mergesort(left)
        mergesort(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
# these while loops for remaining elemnts in left ,right sub array
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr 
arr = [20, 50, 74, 1, 6]
mergesort(arr)
print(arr)  # Output: [1, 6, 20, 50, 74]
