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










