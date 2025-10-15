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
    return (wordcount)

def count_char(file):
    with open(file) as f:
        words = f.read().lower()
    return dict(Counter(words))

def print_sort_dict(file):
    with open(file) as f:
        buffer = f.read().lower()
    #keep only alphabetic and accented characters
    filtered = [c for c in buffer if c.isalpha or c in ['æ', 'â', 'ê', 'ë', 'ô', 'ã', 'õ', 'ñ']]    
    dictBuffer = dict(sorted(Counter(filtered).items(), key=lambda item:item[1], reverse=True))
    return(dictBuffer)