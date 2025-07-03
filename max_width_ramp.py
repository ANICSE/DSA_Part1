class Solution:
    def max_width_ramp(self, nums):
        stack = []
        for i, num in enumerate(nums):
            if not stack or num < nums[stack[-1]]:
                stack.append(i)
        max_width = 0
        for j in reversed(range(len(nums))):
            while stack and nums[j] >= nums[stack[-1]]:
                i = stack.pop()
                max_width = max(max_width, j-1)
        return max_width
    
def main():
    so = Solution()
    #nums = [6,0,8,2,1,5]
    nums = [9,8,1,0,1,9,4,0,4,1]
    print(f"MAximum width is: {so.max_width_ramp(nums)}")

if __name__ =="__main__":
    main()