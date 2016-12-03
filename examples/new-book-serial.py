from __future__ import print_function
import re
import random

def line_tokenize(line):
    s = re.sub(r'[^\w\s]','',line)
    l = re.split(r'\s*', s)
    return [w for w in l if len(w) > 0]

def tokens_sample(tkns, n):
    return random.sample(tkns, n)

if __name__ == "__main__":

    # Create a list of tokens in the book.
    f = open('sherlock.txt')
    tokens = []
    for line in f:
        tokens += line_tokenize(line)
    f.close()

    # Create a new, longer book by randomly sampling 100 tokens for
    # every token in this book.
    new_tokens = []
    for i in xrange(len(tokens)):
        new_tokens += random.sample(tokens, 1000)

    print(len(tokens), len(new_tokens))
