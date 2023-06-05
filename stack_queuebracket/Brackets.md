# Code Challenge 13 : stack-queue-brackets

## WhiteBoard:
![](cc13.jpg)

****
## Summary && Description :
The validate_brackets function takes a string as an argument and returns a boolean value indicating whether the brackets in the string are balanced or not. It checks for three types of brackets: round brackets (), square brackets [], and curly brackets {}.

The function iterates through each character in the input string. If the character is an opening bracket (one of '(', '[', or '{'), it is added to a stack. If the character is a closing bracket (')', ']', or '}'), the function checks if the stack is empty. If the stack is empty, it means there is no corresponding opening bracket for the closing bracket, and the function returns False.

If the stack is not empty, the function pops the topmost opening bracket from the stack and checks if it matches the current closing bracket. If the brackets do not match, the function returns False.

After iterating through all the characters, the function checks if there are any remaining opening brackets in the stack. If the stack is empty, it means all opening brackets have been matched with their corresponding closing brackets, and the function returns True. Otherwise, it returns False.
***
## approach and effenciy:
Big(o): Time complexity :O(n)
Big(o): space complexity :O(1)

*****
[Link To my code ]()