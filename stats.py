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

def dict_split(letter_dict):
    split_dict = []
    for ch, num in letter_dict.items():
        split_dict.append({"char": ch, "num": num})
    return split_dict

def sort_on(split_dict):
    return split_dict["num"]

def dict_sort(split_dict):
    split_dict.sort(reverse=True, key=sort_on)
    return split_dict
    