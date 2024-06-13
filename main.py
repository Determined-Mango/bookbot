def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)                                         # Print the entire book
    print("Word count:", count_words(text))             # Print the word count from count_words function
    print("Character count:", count_characters(text))   # Print the character count from count_characters function


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

main()