floor = 1
max_floor = 4

while floor <= max_floor:
    if floor == 2:
        print("Floor 2 skipped")
        floor += 1
        continue
    print(f"Checking floor {floor}")
    floor += 1

print("Inspection complete")