import nltk.data

# Load the sentence tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

# Get the input text
text = input()

# Tokenize the text into sentences
sentences = tokenizer.tokenize(text)

# Print the list of sentences
print(sentences)