class Solution:
    def intPalindrome(self, x: int)-> bool:
        if x < 0 or (x!=0 and x%10==0):
            return False
        
        rev_half = 0
        while x >  rev_half:
            rev_half = (rev_half * 10) + (x%10)
            x//= 10
        
        return x == rev_half or x == rev_half//10
    
def main():
    sol = Solution()
    x = 123
    print(f"Palindrome of {x} is: {sol.intPalindrome(x)}")
    
if __name__ =="__main__":
    main()