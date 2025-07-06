from typing import List
from collections import Counter

class Solution:
    def minimum_window_substring(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_count = Counter(t)
        min_lef = float('inf')
        result = ""

        #try all substring
        for i in range(len(s)):
            for j in range(i+1, len(s) +1):
                window = s[i:j]
                window_count = Counter(window)

                #Check if window covers all character of t
                if all(window_count[char] >= t_count[char] for char in t_count):
                    if (j-i) < min_lef:
                        min_lef = j - i
                        result = window
        
        return result
    
def main():
    sol = Solution()
    s= "ADOBECODEBANC"
    t = "BCD"

    print(f"Mximum window: {sol.minimum_window_substring(s, t)}")

if __name__ == "__main__":
    main()