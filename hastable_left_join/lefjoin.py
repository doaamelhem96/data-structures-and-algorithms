def left_join(synonyms, antonyms):
    result = []
    for key in synonyms:
        synonym_value = synonyms[key]
        antonym_value = antonyms.get(key, None)  # Get the value from the antonyms hashmap or return None if key not found

        # Append the key and values to the result list
        if antonym_value is not None:
            result.append([key, synonym_value, antonym_value])
        else:
            result.append([key, synonym_value, None])

    return result

# Test cases
def test_left_join():
    synonyms = {
        "diligent": "employed",
        "fond": "enamored",
        "guide": "usher",
        "outfit": "garb",
        "wrath": "anger"
    }

    antonyms = {
        "diligent": "idle",
        "fond": "averse",
        "guide": "follow",
        "flow": "jam",
        "wrath": "delight"
    }

    # Test case 1
    expected_output = [
        ["diligent", "employed", "idle"],
        ["fond", "enamored", "averse"],
        ["guide", "usher", "follow"],
        ["outfit", "garb", None],
        ["wrath", "anger", "delight"]
    ]
    assert left_join(synonyms, antonyms) == expected_output

    # Test case 2: When antonyms hashmap is empty
    antonyms = {}
    expected_output = [
        ["diligent", "employed", None],
        ["fond", "enamored", None],
        ["guide", "usher", None],
        ["outfit", "garb", None],
        ["wrath", "anger", None]
    ]
    assert left_join(synonyms, antonyms) == expected_output

    # Test case 3: When synonyms hashmap is empty
    synonyms = {}
    antonyms = {
        "flow": "jam",
        "wrath": "delight"
    }
    expected_output = []
    assert left_join(synonyms, antonyms) == expected_output

    print("All test cases passed!")

# Run the test cases
test_left_join()
