import json

# Read JSON data from standard input
data = json.loads(input())

# Initialize a dictionary to count the stops for each bus_id
stops_per_line = {}

# Count the stops for each bus_id
for entry in data:
    bus_id = entry["bus_id"]
    stops_per_line[bus_id] = stops_per_line.get(bus_id, 0) + 1

# Print the result
print("Line names and number of stops:")
for bus_id, stops in sorted(stops_per_line.items()):
    print(f"bus_id: {bus_id}, stops: {stops}")
