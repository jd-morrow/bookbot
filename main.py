import sys
from stats import get_word_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    letter_count = get_letter_count(text)
    sorted_chars = sort_letter_count(letter_count)

    print(f"In the submitted text at {book_path} there are...")
    print(f"{word_count} words found in the document, and...")
    for char in sorted_chars:
        if char["Character"].isalpha():
            print(f"{char['Character']}: {char['Count']}")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_letter_count(text):
    lowered = text.lower()
    char_count = {}
    for char in lowered:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(a):
    return a["Count"]

def sort_letter_count(char_count):
    sorted = []
    for char in char_count:
        sorted.append({"Character": char, "Count": char_count[char]})
    sorted.sort(reverse=True, key=sort_on)
    return sorted

main()