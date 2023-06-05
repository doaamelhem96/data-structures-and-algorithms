import pytest
from brackets import validate_brackets


def test_validate_brackets0(): # function to check true statement
    actual=validate_brackets("[]")
    expected = True
    assert actual == expected
def test_valdate_brackets1(): # function to check false statement
    actual=validate_brackets("[{]}")
    expected= False
    assert actual==expected
def test_valdate_brackets2(): # function to check if there is no closing char
    actual=validate_brackets("{")
    expected= False
    assert actual==expected 
def test_valdate_brackets3():
    actual= validate_brackets(")")# function to check if there is no opining char 
    expected =False
    assert actual==expected