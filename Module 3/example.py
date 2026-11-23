for group in range(1, 3):
    for match in range(1, 3):
        print(f"G{group}-M{match}")

# stage |   arena   |   stage * arena   |   total_points після додавання 
#   1         1                1                         1  
#   1         2                2                         3   
#   1         3                3                         6
# After stage 1: 6
#   2         1                2                         8
#   2         2                4                         12
#   2         3                6                         18
# After stage 2: 18 