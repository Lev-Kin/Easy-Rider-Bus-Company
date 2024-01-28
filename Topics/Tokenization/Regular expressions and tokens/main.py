import re

text = input()

# Use the regular expression to find the tokens
tokens = re.findall(r"[A-z'-]+", text)

# Print the list of tokens
print(tokens)
