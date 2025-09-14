from stats import number_of_words, number_of_charecters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_text = f.read()
        return book_text

def main():
    path_to_file = "books/frankenstein.txt"
    book_text_file = get_book_text(path_to_file)
    word_count = number_of_words(book_text_file)
    char_count = number_of_charecters(book_text_file)
    print(f"{word_count} words found in the document")
    print(f"{char_count} characters found in the document")

main()
