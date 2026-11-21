points = 2500

if points > 2000:
    badge = "Legend"
elif points > 1500:
    badge = "Veteran"
elif points > 500:
    badge = "Active"
else:
    badge = "Newcomer"

print(f"Badge: {badge}")