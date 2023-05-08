def insertShiftArray(arr, value):
    n = len(arr)
    middle = n // 2
    array = [None] * (n + 1)
    
    if n % 2 == 0:
        i = 0
        while i < middle:
            array[i] = arr[i]
            i += 1
        
        array[middle] = value
        
        while i < n:
            array[i + 1] = arr[i]
            i += 1
    else:
        i = 0
        while i <= middle:
            array[i] = arr[i]
            i += 1
        
        array[middle + 1] = value
        
        while i < n:
            array[i + 1] = arr[i]
            i += 1
    
    return array

"""*****"""
def removeShiftArray(z):
    n = len(z)
    middle = n // 2
    nz = [None] * (n - 1)
    i = 0
    j = 0

    if n % 2 == 0:
        while i < n:
            if i != middle:
                nz[j] = z[i]
                j += 1
            i += 1
    else:
        while i < n:
            if i != middle + 1:
                nz[j] = z[i]
                j += 1
            i += 1
    
    return nz

if __name__=="__main__":
   arr2 = [2, 4, 6, 7, 8]
   print(f" my origin array is <<<\t{arr2}\t>>>, My_array will become after insert and shiftting is <<<{insertShiftArray(arr2,0)}>>>\n******")
   print(f"******\n my origin array is <<<\t{arr2}\t>>> , My_array will become after remove middle element and filling the gaps is <<<{removeShiftArray(arr2)}>>>")

 