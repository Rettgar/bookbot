import sys
print(sys.argv)
if len(sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)
    
book = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        return f.read()
    # this reads the book

def main():
    book_text = get_book_text(sys.argv[1])
    counts = character_count(book_text)
    sorted_counts = sorted(counts.items(), key=lambda letter: letter[1], reverse=True)
    print(f'Analyzing book found at {book}')
    print(f'----------- Word Count ----------')
    print(f'Found {number_of_words(book_text)} total words')
    for char, count in sorted_counts:
        if char.isalpha():
            print(f'{char}: {count}')
    print(f'============= END ===============')
    
from stats import number_of_words
from stats import character_count

main()


