import sys
from collections import Counter
from typing import Dict, List
from stats import get_word_count

def get_book_text(path: str) -> str:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at path '{path}'")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def get_character_counts(text: str) -> Counter:
    return Counter(text.lower())

def sort_character_counts(char_counts: Counter) -> List[Dict[str, int]]:
    char_list = [{"Character": char, "Count": count} for char, count in char_counts.items()]
    char_list.sort(reverse=True, key=lambda item: item["Count"])
    return char_list

def generate_report(book_path: str, word_count: int, sorted_chars: List[Dict[str, int]]) -> None:
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    print("Character counts (alphabetic only, descending):")
    for item in sorted_chars:
        char = item["Character"]
        if isinstance(char, str) and char.isalpha():
            print(f"The '{char}' character was found {item['Count']} times")

    print("--- End report ---")

def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    print(f"Processing book: {book_path}")
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_counts = get_character_counts(text)
    sorted_character_list = sort_character_counts(character_counts)

    generate_report(book_path, word_count, sorted_character_list)

if __name__ == "__main__":
    main()