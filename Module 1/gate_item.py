item_code = "POTION_50"
prefix = item_code[0:6]
code_length = len(item_code)
is_valid = prefix == "POTION" and code_length > 8
print(f"Valid potion: {is_valid}")