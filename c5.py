# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

# Read input
month, day, year = map(int, input().split())

# Get the day of the week (0 = Monday, 6 = Sunday)
day_index = calendar.weekday(year, month, day)

# Convert to day name in uppercase
print(calendar.day_name[day_index].upper())
