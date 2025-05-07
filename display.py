def dispay_list(list):
    for item in list:
        print(f"{item["char"]}: {item["num"]}")

def display_usage_error():
    print("Usage: python3 main.py <path_to_book>")

def display_title():
    print("============ BOOKBOT ============")

def display_analyze(path):
    print(f"Analyzing book found at {path}...")

def display_word_count(count):
    print("----------- Word Count ----------")
    print(f"Found {count} total words")


def display_characters(characters):
    print("--------- Character Count -------")
    dispay_list(characters)

def display_end():
    print("============= END ===============")

def display_info(path, words_count, characters_list):
    display_title()
    display_analyze(path)
    display_word_count(words_count)
    display_characters(characters_list)
    display_end()