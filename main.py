from stats import get_book_word_count, get_book_characters
from display import display_info, display_usage_error
from sys import argv, exit

def get_book_text(file_path): 
    with open(file_path) as f:
        return f.read()


def main():
    if len(argv) != 2: 
        display_usage_error()
        exit(1)

    book_content = get_book_text(argv[1])
    words_count = get_book_word_count(book_content)
    characters = get_book_characters(book_content)
    display_info(argv[1], words_count, characters)

main()