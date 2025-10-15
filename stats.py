from collections import Counter
def get_book_text(filename):
    with open(filename) as f:
        print(f.read())

def count_words(file):
    wordcount = 0
    with open(file) as f:
        book = f.read()
        words = book.split()
        wordcount += len(words)
    return print(f"Found {wordcount} total words")

def count_char(file):
    with open(file) as f:
        words = f.read().lower()
    return print(dict(Counter(words)))