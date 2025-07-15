class Solution:
    def longestValidParentheses(self, s: str)->int:
        l_count = r_count = max_len = 0
        i = 0

        while i < len(s):
            if s[i] =="(":
                l_count +=1
            else:
                r_count +=1
            
            if l_count == r_count:
                max_len = max(max_len, l_count+r_count)
            elif r_count > l_count:
                l_count = r_count = 0

            i +=1

        #check in the opposite direction:
        l_count = r_count = 0
        i = len(s) - 1
        while i >=0:
            if s[i] =="(":
                l_count +=1
            else:
                r_count +=1
            
            if l_count == r_count:
                max_len = max(max_len, l_count+r_count)
            elif l_count > r_count:
                l_count = r_count = 0

            i -=1

        return max_len
    
def main():
    sol = Solution()
    test_cases = [
        "(()",         # 2
        ")()())",      # 4
        "",            # 0
        "()(()",       # 2
        "((()))",      # 6
        "(()())",      # 6
        "())((())",    # 4
        "(((((((((",   # 0
    ]

    for s in test_cases:
        print(f"'{s}' → {sol.longestValidParentheses(s)}")

if __name__ == "__main__":
    main()