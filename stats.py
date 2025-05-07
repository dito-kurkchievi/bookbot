def get_book_word_count(text):
    return len(text.split())


def get_book_characters(text):
    words = text.split()
    result = {}

    for word in words:
        symbols = list(word)
        
        for s in symbols:
            lower = s.lower()
            if lower in result:
                result[lower] += 1
            else:
                result[lower] = 1

    return sort_books(transform_character_dict_to_array(result))

def sort_on(dict):
    return dict["num"]

def transform_character_dict_to_array(dict):
    result = []
    
    for key in dict:
        if key.isalpha():
            result.append({ "char": key, "num": dict[key] })

    return result

def sort_books(list):
    list.sort(reverse=True, key=sort_on)
    return list