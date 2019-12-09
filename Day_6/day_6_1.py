objects = []
orbit_counts = {}
with open("day_6.txt", "r") as fileStream:
    for line in fileStream:
        objects.append(line.strip("\n").split(")"))

for orbit_pair in objects:
    orbit_object = orbit_pair[1]
    next_orbit = orbit_pair[0]

    if orbit_object in orbit_counts:
        break

orbit_count = 1
found_next_orbit = True
while found_next_orbit:
    found_next_orbit = False
    for orbit_pair2 in objects:
        if orbit_pair2[1] == next_orbit:
            next_orbit = orbit_pair2[0]
            orbit_count += 1
            found_next_orbit = True
            break
orbit_counts[orbit_object] = orbit_count

print(orbit_counts)
print(sum(orbit_counts.values()))