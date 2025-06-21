from collections import defaultdict

def grp_anagrams(strs):
    anagrams = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(s))
        anagrams[key].append(s)
    return list(anagrams.values())

def main():
    print("Grouping Anagrams")
    strs = ["eat","tea","tan","ate","nat","bat", "cat"]
    print(grp_anagrams(strs))
if __name__ == "__main__":
    main()