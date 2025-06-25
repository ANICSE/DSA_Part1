class Solution:
    def longestPlindrome(self, s:str) ->int:
        counts = {}
        for c in s: 
            counts[c] =counts.get(c,0) + 1

        result, odd_found = 0, False
        for _, c in counts.items(): # _ ->key, c ->values
            if c%2 == 0:
                result+= c
            else:
                result+= c - 1
                odd_found = True
        if odd_found:
            result+= 1
        return result
    
def main():
    sol =Solution()
    s = "aaaabbbbbb"
    print(f"longest palindrome for {s} is : {sol.longestPlindrome(s)}")

if __name__ == "__main__":
    main()
        
