members = int(input("Enter number of members: "))
curr = 1
has_afk = False

while curr <= members:
    points = int(input(f"Enter points for member {curr}: "))
    if points == 0:
        has_afk = True
    curr += 1

if not has_afk:
    print("Team qualifies")
else:
    print("Team disqualified")