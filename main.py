from stats import get_word_count
from stats import get_letter_count

def get_book_text(book_path):
    with open(book_path) as b:
        book_contents = b.read()
        return book_contents

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = get_word_count(book_text)
    print(f"Found {word_count} total words")
    letter_dict = get_letter_count(book_text)
    print(letter_dict)

main()