import re


def extract_data(string):
    start_match = re.search("<START>", string)
    end_match = re.search("<END>", string)

    if start_match and end_match:
        start_pos = start_match.end()
        end_pos = end_match.start()
        return string[start_pos:end_pos]
    else:
        return None


# Get the input string
string = input()

# Extract the data
extracted_data = extract_data(string)

# Print the extracted data
if extracted_data:
    print(extracted_data)
else:
    print("No data found between tags.")
