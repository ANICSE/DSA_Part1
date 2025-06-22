def is_subsequence(source, target):
    i, j = 0, 0
    while i < len(source) and j < len(target):
        if source[i] == target[j]:
            i+=1
        j +=1
    
    # It returns True if all characters in s have been matched (i.e., i has advanced past the last character of s).
    # It returns False if not all characters in s were found in t in order.
    return i == len(source)

def main():
    source = "abc"
    target = "ahcgdb"
    print(f"{source} is a subsequence of {target} ? {is_subsequence(source, target)}")

if __name__ == "__main__":
    main()