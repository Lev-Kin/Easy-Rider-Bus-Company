import re

string = input()

capitalized_words = re.findall(r"\b[A-Z][a-z]*\b|\b[A-Z]+\b", string)

digits = re.findall(r"\d+", string)

print("Capitalized words:", ", ".join(capitalized_words))
print("Digits:", ", ".join(digits))
