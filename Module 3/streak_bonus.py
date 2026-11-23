days = int(input("Enter streak days: "))
curr = 1
points = 0

while curr <= days:
    points += curr * 10
    curr += 1

print(f"Total bonus: {points} points")