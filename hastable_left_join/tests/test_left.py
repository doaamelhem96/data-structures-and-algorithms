import pytest
from hashtable import HashTable
from lefjoin import left_join

def test_left_join_empty():
    synonyms = HashTable()
    antonyms = HashTable()

    result = left_join(synonyms, antonyms)
    assert result.keys() == []

def test_left_join_some():
    synonyms = HashTable()
    synonyms.set("diligent", "employed")
    synonyms.set("fond", "enamored")
    synonyms.set("guide", "usher")

    antonyms = HashTable()
    antonyms.set("diligent", "idle")
    antonyms.set("fond", "averse")
    antonyms.set("guide", "follow")

    result = left_join(synonyms, antonyms)
    assert result.get("diligent") == ("employed", "idle")
    assert result.get("fond") == ("enamored", "averse")
    assert result.get("guide") == ("usher", "follow")

