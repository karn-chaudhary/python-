
def calculate_happiness(n, m, array, A, B):
    happiness = 0
    A = set(A)
    B = set(B)
    
    for element in array:
        if element in A:
            happiness += 1
        if element in B:
            happiness -= 1
    
    return happiness

# Sample Input
n, m = 3, 2
array = [1, 5, 3]
A = [3, 1]
B = [5, 7]

# Calculate Happiness
result = calculate_happiness(n, m, array, A, B)
print(result)  # Output: 1
