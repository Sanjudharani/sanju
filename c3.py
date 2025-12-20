# Enter your code here. Read input from STDIN. Print output to STDOUT
# Read number of test cases
for _ in range(int(input())):
    try:
        a, b = input().split()           # Read the two inputs
        a = int(a)                       # Convert first input to int
        b = int(b)                       # Convert second input to int
        print(a // b)                    # Perform integer division
    except (ZeroDivisionError, ValueError) as e:
        print("Error Code:", e)          # Print the error message