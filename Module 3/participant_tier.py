role = input("Enter role: ")
points = int(input("Enter points: "))
if role != "student":
    print("Not a participant")
elif points < 0:
    print("Invalid points")
elif points <= 50:
    print("Beginner")
elif points >= 100:
    print("Pro")
else:
    print("Intermediate")