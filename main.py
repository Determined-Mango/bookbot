def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    char_count = count_characters(text)

    # Convert dictionary to list of dictionaries
    char_list = convert_dict_to_list(char_count)

    # Sort the list by 'num' in descending order
    char_list.sort(reverse=True, key=lambda x: x['num'])

    # Print the report
    print_report(book_path, word_count, char_list)


def get_book_text(path):
    with open(path) as f:
        return f.read()

# Opens the file at the given path and returns its entire content as a string

def count_words(text):
    return len(text.split())

# Splits the string from get_book_text into a list of words using whitespace as the delimiter and returns the number of words (elements in the list)

def count_characters(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():
            if char in char_count:
                char_count[char] +=1
            else:
                char_count[char] = 1
    return char_count                

def convert_dict_to_list(char_count):
    char_list = []
    for char, num in char_count.items():
        char_list.append({'character': char, 'num': num})
    return char_list


def print_report(book_path, word_count, char_list):
    # Prints the header
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")

    # Print each character's count
    for entry in char_list:
        print(f"The '{entry['character']}' character was found {entry['num']} times")

    # Print the footer
    print(f"--- End Report ---")


main()