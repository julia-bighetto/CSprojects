
import random

def create_dictionary(filename):
    """ takes a string representing the name of a text file and returns
        a dictionary of key-value pairs
    """
    file = open(filename, 'r')
    text = file.read()
    file.close()
    words = text.split()
    d = {}
    current_word = '$'
    for next_word in words:
        if current_word not in d:
            d[current_word] = [next_word]
        else:
            d[current_word] += [next_word]
        if '.' in next_word:
            current_word = '$'
        elif '!' in next_word:
            current_word = '$'
        elif '?' in next_word:
            current_word = '$'
        else:
            current_word = next_word
    return d

def generate_text(word_dict, num_words):
    """ takes as parameters a dictionary of word transitions word_dict and
        a positive integer named num_words. It returns a string of num_words
        words
    """
    current_word = '$'
    while num_words != 0:
        next_word = random.choice(word_dict[current_word])
        print(next_word, end=' ')
        if '.' in next_word:
            current_word = '$'
        elif '!' in next_word:
            current_word = '$'
        elif '?' in next_word:
            current_word = '$'
        else:
            current_word = next_word
        num_words -= 1
    print()
    
    
