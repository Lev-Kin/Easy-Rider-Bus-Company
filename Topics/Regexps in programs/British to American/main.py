import re

string = input()

pattern = r"(\b\w*?o)u(\w*?\b)"

americanized_string = re.sub(pattern, lambda match: match.group(1) + match.group(2), string)

print(americanized_string)