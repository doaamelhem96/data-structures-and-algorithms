from repeated_word import repeated_word
from Hashtable.hashtable import *
import pytest

def test_repeated_word():
   
    input_string1 = "Duaa Z Melhem , Duaa ."
    assert repeated_word(input_string1) == "duaa"

    

    input_string3 = "This is Duaa Melhem , my major is computer Science "
    assert repeated_word(input_string3) == "is"

    # Edge cases
    assert repeated_word("") is None  # Empty string
    assert repeated_word("word") is None  # Single word
    
 
    input_string4 = "This is a Test tESt"
    assert repeated_word(input_string4) == "test"  

    input_string5 = "Case case Case"
    assert repeated_word(input_string5) == "case"  
test_repeated_word()
