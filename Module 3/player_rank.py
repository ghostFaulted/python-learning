rating = int(input("Enter rating: "))
if rating > 2000:
    print("Gold")
elif rating > 1000:
    print("Silver")
else:
    print("Bronze")