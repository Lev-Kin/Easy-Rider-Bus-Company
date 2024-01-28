import re

string = input()
pets = re.compile(r'dog|cat|parrot|hamster', re.IGNORECASE)
found_pets = pets.findall(string)
print(found_pets)
