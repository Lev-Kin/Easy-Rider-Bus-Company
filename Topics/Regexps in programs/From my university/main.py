import re

email_line = input()  # This will work in a local Python environment, not here
# Check if the email is from the university domain 'ucsc.cl'
is_from_university = bool(re.search(r'From: \S+@ucsc\.cl', email_line))

print(is_from_university)
