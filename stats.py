def number_of_words(book_text):
    return len(book_text.split())


def character_count(book_text):
    char_count = {}
    for character in book_text:
        character = character.lower()
        if character in char_count:
            char_count[character] += 1
        else:
            char_count[character] = 1
    return(char_count)


