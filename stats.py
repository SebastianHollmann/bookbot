def number_of_words(book_text_file):
    number_of_word = len(book_text_file.split())
    return number_of_word

def number_of_charecters(book_text_file):
    text_lowercased = book_text_file.lower()
    dic_of_charecters = {}
    for i in text_lowercased:
        if i in dic_of_charecters:
            dic_of_charecters[i] += 1
        else:
            dic_of_charecters[i] = 1
    return dic_of_charecters

def sort_charecters(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    def get_num(item):
        return item["num"]

    char_list.sort(key=get_num, reverse=True)
    return char_list
