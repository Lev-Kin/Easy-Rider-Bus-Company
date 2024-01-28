import re


def is_valid_username(username):
    pattern = r"^[a-zA-Z]"  # Regex pattern matching a letter at the beginning
    return re.match(pattern, username)


# Get the username
username = input()

# Check if the username is valid
if is_valid_username(username):
    print("Thank you!")
else:
    print("Oops! The username has to start with a letter.")
