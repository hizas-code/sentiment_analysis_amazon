from nltk import TreebankWordTokenizer

def tokenizing(words):
    tokenizer = TreebankWordTokenizer()
    tokens = tokenizer.tokenize(words)
    return tokens
