import re
<<<<<<< HEAD

def tokenize_string(input_string):
    # Removing all non-alphanumeric characters and normalize spaces
    words = re.findall(r'\b\w+\b', re.sub(r'[^\w\s]', ' ', input_string.lower()))
    return words

def count_word_frequency(word_list):
    word_freq = {}
    for word in word_list:
        word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def find_first_repeated_word(word_list, word_freq):
    for word in word_list:
        if word_freq[word] > 1:
            return word
    return None

def repeated_word(input_string):
    words = tokenize_string(input_string)
    word_freq = count_word_frequency(words)
    return find_first_repeated_word(words, word_freq)

<<<<<<< HEAD
# Test cases
assert repeated_word("Once upon a time, there was a brave princess who...") == "a"
assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == "it"
assert repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") == "summer"
assert repeated_word("this is an Code Challenge 31 and is about The Hastable") == "is"
=======
>>>>>>> 707220ae4258d7bab9c7f3b04bc15e220e8ba493
=======
from Hashtable.hashtable import *

def repeated_word(input_string):
    # Create a set to keep track of seen words
    seen_words = set()
    
    # Split the input string into words
    words = input_string.split()

    for word in words:
        # Remove any non-alphanumeric characters from the word
        cleaned_word = ''.join(filter(str.isalnum, word)).lower()
        
        # Check if the cleaned word has been seen before
        if cleaned_word in seen_words:
            return cleaned_word
        else:
            seen_words.add(cleaned_word)
    
    return None

# Test assertions
assert repeated_word("Once upon a time, there was a brave princess who...") == "a"
assert repeated_word("It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only...") == "it"
assert repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") == "summer"

print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York...") )
>>>>>>> 622084ca6c3403699e3a0e8e40391085fbdd8f08
