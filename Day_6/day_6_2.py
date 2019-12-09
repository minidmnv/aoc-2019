objects = []
orbit_counts = {}
orbits = dict()
with open("day_6.txt", "r") as fileStream:
    for line in fileStream:
        objects.append(line.strip("\n").split(")"))

for orbit_pair in objects:
    orbit_object = orbit_pair[1]
    if orbit_object != "YOU" and orbit_object != "SAN":
        continue

next_orbit = orbit_pair[0]
orbits[orbit_object] = set()
while next_orbit != "COM":
    for orbit_pair2 in objects:
        if orbit_pair2[1] == next_orbit:
            orbits[orbit_object].add(next_orbit)
            next_orbit = orbit_pair2[0]

print(len(orbits["YOU"]) + len(orbits["SAN"]) - 2 * len(orbits["YOU"] & orbits["SAN"]) )