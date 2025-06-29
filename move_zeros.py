from typing import List

class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        left = 0
        
        for right in range(len(nums)):
            #nums[right] check if its falsy: '0', 'False', 'None'
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
        return nums
    
    def removeElement(self, nums:List[int], val: int)-> int:
        left = 0

        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left+= 1
        return left
    
    def arrayOperations(self, nums: List[int])-> List[int]:

        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        left = 0
        for right in range(len(nums)):
            if nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                
        return nums

def main():
    sol = Solution()
    nums = [0, 1, 0, 3, 12]
    print(nums)
    sol.moveZeros(nums)
    print(nums)
    print("Problem Statement 2:")
    nums1 = [3, 2, 2, 3]
    remo = sol.removeElement(nums1, val=3)
    print(remo)
    print("Problem Statement 3:")
    nums2 = [1, 2, 2, 1, 1, 0]
    print(f"After operations on array {nums2}, the result is: {sol.arrayOperations(nums2)}")

if __name__ == "__main__":
    main()