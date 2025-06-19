from stats import get_word_count, get_letter_count, sort_chars
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit("-1")
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = get_word_count(book_text)
    letter_count = get_letter_count(book_text)
    sorted_chars = sort_chars(letter_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words ")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
    return text

main()
