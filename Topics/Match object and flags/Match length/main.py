import re

template = r"are you ready??.?.?"

# Read the input string
string = input()

# Try to match the template
match = re.match(template, string)

# Check if there is a match
if match:
    # Get the length of the matched substring
    length = match.end() - match.start()

    # Print the length
    print(length)
else:
    # No match found
    print(0)