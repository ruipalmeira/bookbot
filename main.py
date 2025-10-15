from stats import count_words, count_char, get_book_text, print_sort_dict
def main():
    file = "books/frankenstein.txt"
    #get_book_text(file)
    wordcount = count_words(file)
    charcount = print_sort_dict(file)
    ordered = {}
    print(f"============ BOOKBOT ============ \n Analyzing book found at {file}...")
    print(f"----------- Word Count ----------\n Found {wordcount} total words")
    print("--------- Character Count -------")
    for char, count in charcount.items():
        print(f"{char}: {count}")
    print("\n============= END ===============")
if __name__ == '__main__':
    main()