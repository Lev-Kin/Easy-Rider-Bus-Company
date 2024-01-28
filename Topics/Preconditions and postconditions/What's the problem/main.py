import re

string = input()
pattern = "(?<=@)\w+"
results = re.search(pattern, string)

if results:
    print(results.group())
else:
    print("No match found")