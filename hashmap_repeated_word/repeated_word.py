import re

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
