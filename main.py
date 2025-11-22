import sys
from stats import print_char_count, words, char_count


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        print(f"Analyzing book found at {path_to_file}...")
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_txt = get_book_text(sys.argv[1])
    words(book_txt)
    count = char_count(book_txt)
    print_char_count(count)
    print("============= END ===============")


main()
