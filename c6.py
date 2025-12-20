from collections import Counter

if __name__ == '__main__':
    s = input()
    
    # Count occurrences of each character
    counter = Counter(s)
    
    # Sort by descending frequency, then alphabetically
    for char, freq in sorted(counter.items(), key=lambda x: (-x[1], x[0]))[:3]:
        print(char, freq)
