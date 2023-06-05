def validate_brackets(string):# define methods which called validate_brackets and has one arguments it's type "string" 

    list = [] # define empty_list 
    list_opening_brackets = ["(", "[", "{"] #define list for opening brackets
    list_closing_brackets = [")", "]", "}"]#define list for opening brackets
    bracket_pairs = {"(": ")", "[": "]", "{": "}"} #define dictionary  for opening brackets and closing brackets 

    for char in string: # this for loop to look up into every elemnts in string arguemnts ,, Notice thate python treat with string like list which means any string has {index and values} 
        if char in list_opening_brackets: # check if this char in list of opening bracktes then {append} it in list var
            list.append(char)
        elif char in list_closing_brackets: # check if this char in closing list if is it in closing list then ??
            if not list: # check if empty list returnes false  
                return False
            last_opening_bracket = list.pop() # else pop first char from list
            if bracket_pairs[last_opening_bracket] != char: # comparing between char and list elemnts if not equals each others returnes false 
                return False

    return len(list) == 0 # to check if there any remaining bracket in list



print(validate_brackets("{}"))  # True
print(validate_brackets("{}(){}"))  # True
print(validate_brackets("()[[Extra Characters]]"))  # True
print(validate_brackets("(){}[[]]"))  # True
print(validate_brackets("{}{Code}[Fellows](())"))  # True
print(validate_brackets("[({}]"))  # False
print(validate_brackets("(]("))  # False
print(validate_brackets("{(})"))  # False
