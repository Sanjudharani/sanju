

# Complete the solve function below.
def solve(s):
    words = s.split(' ')
    cap_words = [w.capitalize() for w in words]
    return " ".join(cap_words)

