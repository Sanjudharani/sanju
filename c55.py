if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    # Remove duplicates by converting to a set
    unique_scores = list(set(arr))
    
    # Sort the scores in descending order
    unique_scores.sort(reverse=True)
    
    # The runner-up score is the second element
    print(unique_scores[1])
