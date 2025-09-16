import sys
from stats import number_of_words, number_of_charecters, sort_charecters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
        return book_text

def path_to_file_check():
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    path_to_file = path_to_file_check()
    book_text_file = get_book_text(path_to_file)
    word_count = number_of_words(book_text_file)
    char_count = number_of_charecters(book_text_file)
    char_report = sort_charecters(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_report:
        print(f"{item["char"]}: {item["num"]}")

main()
