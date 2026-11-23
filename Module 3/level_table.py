max_level = int(input("Enter max level: "))
count = 1

while count <= max_level:
    print(f"Level {count}: {count * 100} XP")
    count = count + 1

print("Table complete")