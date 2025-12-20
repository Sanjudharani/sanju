# Enter your code here. Read input from STDIN. Print output to STDOUT
# Number of stamps
n = int(input())

# Create an empty set to store distinct countries
countries = set()

# Read each country name and add to the set
for _ in range(n):
    country = input().strip()
    countries.add(country)

# The size of the set = number of distinct country stamps
print(len(countries))
