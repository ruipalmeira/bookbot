from stats import count_words, count_char, get_book_text
def main():
    file = "books/frankenstein.txt"
    #get_book_text(file)
    count_words(file)
    count_char(file)
if __name__ == '__main__':
    main()