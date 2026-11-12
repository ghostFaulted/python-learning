base_power = 9000
calculated_power = int("9000")
print(f"Same value: {base_power == calculated_power}")
print(f"Same object: {base_power is calculated_power}")
alias_power = base_power
print(f"Alias is same object: {alias_power is base_power}")