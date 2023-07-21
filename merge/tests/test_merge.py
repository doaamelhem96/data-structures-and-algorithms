import pytest
from merge import mergesort
def test_merge():
    actuall= mergesort([10,2,4,30])
    expected= [2,4,10,30]
    assert actuall==expected
