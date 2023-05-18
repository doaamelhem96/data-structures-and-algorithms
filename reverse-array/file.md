# Reverse-Array
*********
Description:
Reversing an array in Python refers to the process of rearranging the elements of an array in the reverse order. The first element becomes the last, the second becomes the second last, and so on. It is a common operation in programming when you need to change the order of elements in an array.

Summary:
Reversing an array in Python involves rearranging the elements of the array in the opposite order. This can be achieved using reverseArray function ,, without using any built-in function ass append to push the elements of array in another array
*****
# Whiteboard Process

*****
*****
![](Whiteboard.jpg)
## Approach:
The reverseArray function takes an array as input and reverses its elements by using a two-pointer approach. It initializes a new array reversed_Array with the same length as the input array. Then, it uses two pointers, start_Index and end_Index, to iterate through the input array from both ends. The function swaps the elements between the start_Index and end_Index positions, gradually moving towards the center of the array. This process continues until the start_Index surpasses the length of the array.

## Efficiency:

Time Complexity: The time complexity of this approach is O(n), where n is the length of the input array. The function needs to iterate through the entire array once to reverse it.
Space Complexity: The space complexity is O(n) as well. The function creates a new array reversed_Array of the same length as the input array to store the reversed elements.
Overall, the function efficiently reverses the elements of the input array in-place, without requiring any additional space.
********
## Solution
[Link to Code](data.py)

-----------
# psuecode :
def reverseArray(arr):
    reversed_Array = [None] *len(arr)
    start_Index = 0
    end_Index = len(arr) - 1
    while start_Index < len(arr):
        reversed_Array[start_Index] = arr[end_Index]
        start_Index += 1
        end_Index-= 1 
        
        print (reversed_Array)
    print (f"""************************************************************************ \nThe original array was: {arr}\tThe reversed arrray is: {reversed_Array}
    *********************************************************************
            """)
    



        
         
fruits = ["apple", "banana", "cherry"]    
if __name__=="__main__":
      
      reverseArray(fruits)    
    
    


# Names=["Dua'a", "Sami","Dana"]
# reverseArray(Names)



















