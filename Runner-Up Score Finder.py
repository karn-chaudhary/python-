# Read the number of participants
n = int(input("Enter the number of participants: "))

# Read the scores as space-separated integers
scores = list(map(int, input("Enter the scores: ").split()))

# Find the runner-up score
runner_up = max([x for x in scores if x != max(scores)])

# Print the runner-up score
print("Runner-Up Score:", runner_up)
