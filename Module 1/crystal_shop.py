total_crystals = int(input("Enter total crystals: "))
upgrade_cost = 15
upgrades_bought = total_crystals // upgrade_cost
crystals_left = total_crystals % upgrade_cost
print(f"Upgrades bought: {upgrades_bought}")
print(f"Crystals left: {crystals_left}")