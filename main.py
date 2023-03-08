import itertools

arr = [i+1 for i in range(12)]

solutions3 = []
solutions4 = []
solutions5 = []
solutions6 = []

# Generate all possible combinations of length 3, 4, 5, and 6 from arr
for i in range(3, 7):
    combinations = itertools.combinations(arr, i)
    
    # Filter out the combinations that don't add up to 26
    valid_combinations = [c for c in combinations if sum(c) == 26]
    
    # Store the valid combinations in the appropriate list
    if i == 3:
        solutions3 = list(valid_combinations)
    elif i == 4:
        solutions4 = list(valid_combinations)
    elif i == 5:
        solutions5 = list(valid_combinations)
    elif i == 6:
        solutions6 = list(valid_combinations)

print("Combinations of length 3 that add up to 26:")
print(solutions3)

print("Combinations of length 4 that add up to 26:")
print(solutions4)

print("Combinations of length 5 that add up to 26:")
print(solutions5)

print("Combinations of length 6 that add up to 26:")
print(solutions6)

solution = [c for c in itertools.combinations(solutions4, 3) if len(set([x for sublist in c for x in sublist])) == len(c) * len(c[0])]
print(solution)
print(len(solution))
