def reverseArray(arr):
    revarray = []
    for i in range(len(arr)-1, -1, -1):
       revarray.append(arr[i])
       print (revarray)
    return revarray

arr2 = [1, 2, 3, 4, 5]

print ('''********************************************
 ****** The reverse Array is :''',reverseArray(arr2))



