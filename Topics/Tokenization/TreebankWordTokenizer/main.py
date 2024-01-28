from nltk import TreebankWordTokenizer as TWT

text = input()

# Create a TreebankWordTokenizer object
tokenizer = TWT()

# Tokenize the input text
tokens = tokenizer.tokenize(text)

# Print the list of tokens
print(tokens)
