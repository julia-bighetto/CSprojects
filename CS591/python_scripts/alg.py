from dic import dictionary

d = dictionary

# For part 1 and 2
def artist_alg(list_of_comments):
    ''' input: list of strings (comments)
        output: float (index)
    '''
    final_index = 0
    for comment in list_of_comments:
        c_ = comment.replace(".", "")   # taking punctuation out
        c_ = c_.replace("!", "")        # taking punctuation out
        c_ = c_.lower()                 # making sure everything is lowercase
        c_ = c_.split(" ")              # separating words
        comment_index = 0
        for word in c_:
            if word in d:
                #print(word, d[word])   # to see the words and each value
                comment_index += d[word]
        final_index += comment_index
    return final_index * 6 / len(list_of_comments)

# For part 3 and 4
def genre_alg(list_of_lists):
    ''' input: list of list of strings (each row is comments for one specific artist, artist's name is the first val)
        output: string of artists in order
    '''

    final_list = {}
    for ls in list_of_lists:
        i = artist_alg(ls)
        final_list[ls[0]] = i
    artists = sorted(final_list, key=final_list.get, reverse=True)
    string = ""
    for i in range(len(artists)):
        if i+1 == 1:
            string += str(i + 1) + "st: " + artists[i] + " -> " + str(round(final_list[artists[i]], 2)) + "\n"
        elif i+1 == 2:
            string += str(i + 1) + "nd: " + artists[i] + " -> " + str(round(final_list[artists[i]], 2)) + "\n"
        elif i+1 == 3:
            string += str(i + 1) + "rd: " + artists[i] + " -> " + str(round(final_list[artists[i]], 2)) + "\n"
        else:
            string += str(i + 1) + "th: " + artists[i] + " -> " + str(round(final_list[artists[i]], 2)) + "\n"

    return(string)
        
        

    
