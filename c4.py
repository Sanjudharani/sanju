from datetime import datetime

# Function to compute absolute difference in seconds
def time_delta(t1, t2):
    # Define the format of the input timestamps
    fmt = "%a %d %b %Y %H:%M:%S %z"
    
    # Parse timestamps into datetime objects
    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)
    
    # Calculate absolute difference in seconds
    return str(int(abs((dt1 - dt2).total_seconds())))

# Read number of test cases
for _ in range(int(input())):
    t1 = input().strip()
    t2 = input().strip()
    print(time_delta(t1, t2))
