from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int])->List[int]:
        #Initialize the res array to 1
        res = [1] * (len(nums))

        #Start with pre-fixing
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        #Next start with postfix:
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
    
def main():
    sol = Solution()
    nums = [1,2,3,4,5]
    print(f"Product of array except self in {nums} is ----> {sol.productExceptSelf(nums)}")

if __name__ == "__main__":
    main()