def get_word_count(book_text):
    words = book_text.split()
    #print(len(words))
    return len(words)

def get_letter_count(words):

    letter_dict = {}
    for word in words:
        word = word.lower()
        if word in letter_dict:
            letter_dict[word] += 1
        else:
            letter_dict[word] = 1
    return letter_dict
