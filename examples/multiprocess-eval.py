import re
import random
from multiprocessing import Pool

def line_tokenize(line):
    s = re.sub(r'[^\w\s]','',line)
    l = re.split(r'\s*', s)
    return [w for w in l if len(w) > 0]

def tokens_sample(tkns, n):
    return random.sample(tkns, n)

if __name__ == "__main__":

    f = open('sherlock.txt')

    # Create a list of tokens in the book.
    tokens = []
    for line in f:
        tokens += line_tokenize(line)

    # Create a new book by randomly sampling 10 tokens for
    # every token in this book.
    new_tokens = []
    for i in xrange(len(tokens)):
        new_tokens += random.sample(tokens, 1000)


    print(len(tokens), len(new_tokens))
