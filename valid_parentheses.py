class Solution:
    def isvalid(self, s:str)->bool:
        stack = []
        closeToOpen = {")" : "(", "}" : "{", "]" :"["}
        #closeToOpen = {"{" : "}"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            
        return True if not stack else False
    
def main():
    sol = Solution()
    # test_cases = [
    #     "()",       # True
    #     "()[]{}",   # True
    #     "(]",       # False
    #     "([)]",     # False
    #     "{[]}",     # True
    #     "({[]})",         # True
    #     "(((("      # False
    # ]

    test_cases = [
        "}{"        # True        
    ]

    for s in test_cases:
        print(f"{s!r} → {sol.isvalid(s)}")

if __name__ == "__main__":
    main()