# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read number of students subscribed to English newspaper
n_english = int(input())

# Read roll numbers of English subscribers and convert to set of integers
english_subs = set(map(int, input().split()))

# Read number of students subscribed to French newspaper
n_french = int(input())

# Read roll numbers of French subscribers and convert to set of integers
french_subs = set(map(int, input().split()))

# Find intersection of both sets (students with both subscriptions)
both_subs = english_subs.intersection(french_subs)

# Print the total number of students with both subscriptions
print(len(both_subs))

