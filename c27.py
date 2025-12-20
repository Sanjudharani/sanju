# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read number of students subscribed to English newspaper
n_english = int(input())

# Read roll numbers of English subscribers and convert to set of integers
english_subs = set(map(int, input().split()))

# Read number of students subscribed to French newspaper
n_french = int(input())

# Read roll numbers of French subscribers and convert to set of integers
french_subs = set(map(int, input().split()))

# Find union of both sets (students with at least one subscription)
all_subs = english_subs.union(french_subs)

# Print the total number of students with at least one subscription
print(len(all_subs))
