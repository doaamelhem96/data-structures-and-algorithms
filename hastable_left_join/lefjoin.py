from hashtable import HashTable  # Import my HashTable class from the previous code

def left_join(synonyms, antonyms): # Declare function called left_joing and it passed 2 args as hashtable instances
    result = HashTable()  # Initialize a new instance from class HashTable to insert the result
    synonym_keys = synonyms.keys()  # Get the keys from the synonyms HashTable

    for key in synonym_keys:
        value1 = synonyms.get(key)
        value2 = antonyms.get(key)
        result.set(key, (value1, value2))

    return result

if __name__ =="__main__":
    synonyms = HashTable()
    synonyms.set("diligent", "employed")
    synonyms.set("fond", "enamored")
    synonyms.set("guide", "usher")
    synonyms.set("outfit", "garb")
    synonyms.set("wrath", "anger")

    antonyms = HashTable()
    antonyms.set("diligent", "idle")
    antonyms.set("fond", "averse")
    antonyms.set("guide", "follow")
    antonyms.set("flow", "jam")
    antonyms.set("wrath", "delight")

    result = left_join(synonyms, antonyms)

    # Print the result
    for key in result.keys():
        value = result.get(key)
        print(f"The Word is: {key},It's Synonym: {value[0]},  It's Antonym: {value[1]}")

 
