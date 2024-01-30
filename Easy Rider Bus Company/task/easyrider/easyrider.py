import json

# Read JSON data from standard input
data = json.loads(input())

# Initialize dictionaries to count the types of stops for each line
start_stops = set()
finish_stops = set()
transfer_stops = {}
line_stops = {}

# Process the data
for entry in data:
    bus_id = entry["bus_id"]
    stop_name = entry["stop_name"]
    stop_type = entry["stop_type"]

    # Count the start and finish stops
    if stop_type == "S":
        if bus_id in line_stops and "S" in line_stops[bus_id]:
            print(f"There is no start or end stop for the line: {bus_id}.")
            exit()
        start_stops.add(stop_name)
        line_stops.setdefault(bus_id, set()).add("S")
    elif stop_type == "F":
        if bus_id in line_stops and "F" in line_stops[bus_id]:
            print(f"There is no start or end stop for the line: {bus_id}.")
            exit()
        finish_stops.add(stop_name)
        line_stops.setdefault(bus_id, set()).add("F")

    # Count the transfer stops
    transfer_stops.setdefault(stop_name, set()).add(bus_id)

# Verify each line has one start and one finish stop
for bus_id, stops in line_stops.items():
    if "S" not in stops or "F" not in stops:
        print(f"There is no start or end stop for the line: {bus_id}.")
        exit()

# Calculate transfer stops
transfer_stops = {stop for stop, buses in transfer_stops.items() if len(buses) > 1}

# Print the results
print(f"Start stops: {len(start_stops)} {sorted(start_stops)}")
print(f"Transfer stops: {len(transfer_stops)} {sorted(transfer_stops)}")
print(f"Finish stops: {len(finish_stops)} {sorted(finish_stops)}")
