class Solution:
    def word_pattern(self, pattern: str, str: str) -> bool:
        char_map, word_map = {}, {}
        n, i = len(pattern), 0
        words = str.split(" ")
        if n!= len(words):
            return False
        
        while i < n:
            c, word = pattern[i], words[i]
            if (c in char_map) != (word in word_map):
                return False
            if (c in char_map):
                if (word_map[word] != c) or (char_map[c] != word):
                    return False
                
            else:
                char_map[c] = word
                word_map[word] = c
            i+=1
        return i==n
            
def main():
    sol = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(f"Does the string follow the pattern? {sol.word_pattern(pattern, s)}")

    pattern2 = "abba"
    s2 = "dog cat cat fish"
    print(f"Does the string follow the pattern? {sol.word_pattern(pattern2, s2)}")
if __name__ == "__main__":
    main()