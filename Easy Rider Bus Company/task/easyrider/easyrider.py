import json
import re

# Read JSON data from standard input
data = json.loads(input())

# Initialize error counters
error_count = {
    "stop_name": 0,
    "stop_type": 0,
    "a_time": 0
}

# Define the regex for stop names and arrival times
stop_name_pattern = re.compile(r'^[A-Z].*(Road|Avenue|Boulevard|Street)$')
a_time_pattern = re.compile(r'^[0-1][0-9]:[0-5][0-9]$|^[2][0-3]:[0-5][0-9]$')

# Validate each entry
for entry in data:
    # Validate stop_name
    if not stop_name_pattern.match(entry["stop_name"]):
        error_count["stop_name"] += 1

    # Validate stop_type
    if entry["stop_type"] not in ["S", "O", "F", ""]:
        error_count["stop_type"] += 1

    # Validate a_time
    if not a_time_pattern.match(entry["a_time"]):
        error_count["a_time"] += 1

# Print the result
total_errors = sum(error_count.values())
print(f"Format validation: {total_errors} errors")
for field, count in error_count.items():
    print(f"{field}: {count}")
