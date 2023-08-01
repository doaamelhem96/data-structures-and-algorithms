from repeated_word import *
import pytest
def test_repeated_word():
    
    input_string1 = "Duaa Z Melhem , Duaa ."
    assert repeated_word(input_string1) == "duaa"

   
    input_string3 = "This is Duaa Melhem , my major is computer Science "
    assert repeated_word(input_string3) == "is"






test_repeated_word()
