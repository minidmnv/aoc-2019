start_point = (0, 0)

wires = []
wire_coordinates = []
with open("day_3.txt", "r") as filestream:
    for line in filestream:
        wires.append(line.strip("\n").split(","))

wire_number = 0
for wire in wires:
    wire_coordinates.append([])
    current_start_point = start_point
    for instruction in wire:
        direction = instruction[0]
        step = int(instruction[1:])
        if direction == 'R':
            for i in range(1, step + 1):
                last_item = (current_start_point[0] + i, current_start_point[1])
                wire_coordinates[wire_number].append(last_item)
        elif direction == 'L':
            for i in range(1, step + 1):
                last_item = (current_start_point[0] - i, current_start_point[1])
                wire_coordinates[wire_number].append(last_item)
        elif direction == 'U':
            for i in range(1, step + 1):
                last_item = (current_start_point[0], current_start_point[1] + i)
                wire_coordinates[wire_number].append(last_item)
        else:
            for i in range(1, step + 1):
                last_item = (current_start_point[0], current_start_point[1] - i)
                wire_coordinates[wire_number].append(last_item)
        current_start_point = last_item
    wire_number += 1

points_of_cut = list(set(wire_coordinates[0]) & set(wire_coordinates[1]))
distances = []

for coordinates in points_of_cut:
    distances.append((coordinates, abs(coordinates[0]) + abs(coordinates[1])))

for closest_point_of_cut in distances:
    print(wire_coordinates[0].index(closest_point_of_cut[0]) + wire_coordinates[1].index(closest_point_of_cut[0]) + 2)