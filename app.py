# Function to find pairs of numbers whose cubes sum up to the target
def find_cube_pairs(target):
    solutions = []  # Was using 'sol', changed it to 'solutions' (makes more sense)
    max_num = round(target ** (1 / 3))  # Fixed: Was using '***', should be '**' for exponentiation

    for a in range(1, max_num + 1):  # Typo fixed: 'ranges' → 'range'
        for b in range(a, max_num + 1):  # Looping over b from a to avoid duplicates
            if a**3 + b**3 == target:  # Fixed: Again, '***' should be '**'
                solutions.append((a, b))  # Was 'sol.append()', changed to 'solutions.append()' to match the list name
    
    return solutions  # Returning the correct list
# Call the function for 1729 (which is famous for this property also known as Hardy-Ramanujan number)
pairs = find_cube_pairs(1729)  # Fixed: Had an extra comma making it a tuple, removed it
# Print the valid pairs
print("Valid cube pairs for 1729:")  # Fixed: Used 'print' instead of 'printf' (Python isn't C)
for a, b in pairs:
    # Fixed the exponent mistake: was printing a² + b² instead of a³ + b³
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  
