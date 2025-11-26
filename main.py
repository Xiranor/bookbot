from stats import get_word_count
from stats import get_letter_count
from stats import dict_split
from stats import dict_sort
from stats import sort_on
import sys

def get_book_text(book_path):
    with open(book_path) as b:
        book_contents = b.read()
        return book_contents

def main():
    try:
        book_text = get_book_text(sys.argv[1])
        word_count = get_word_count(book_text)
        letter_dict = get_letter_count(book_text)
        split_dict = dict_split(letter_dict)
        dict_sorted = dict_sort(split_dict)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for i in range(len(dict_sorted)):
            char = dict_sorted[i]
            if char["char"].isalpha() == True:
                print(f"{char["char"]}: {char["num"]}")
        print("============= END ===============")
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()