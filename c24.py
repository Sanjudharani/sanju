# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read number of students subscribed to English newspaper
n_english = int(input())

# Read roll numbers of English subscribers and convert to set of integers
english_subs = set(map(int, input().split()))

# Read number of students subscribed to French newspaper
n_french = int(input())

# Read roll numbers of French subscribers and convert to set of integers
french_subs = set(map(int, input().split()))

# Find students who have subscriptions to either English or French but not both
either_only = english_subs.symmetric_difference(french_subs)

# Print the total number of such students
print(len(either_only))
