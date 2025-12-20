def merge_the_tools(string, k):
    # your code goes here
     for i in range(0, len(string), k):
        block = string[i:i+k]
        seen = ""
        for ch in block:
            if ch not in seen:
                seen += ch
        print(seen)
