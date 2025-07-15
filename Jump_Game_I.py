from typing import List
class Solution:
    def canJump(self, nums: List[int])-> bool:
        goal = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False
    
def main():
    sol = Solution()
    nums = [2,3,1,1,4]
    print(f"Can jump to the last index in the array {nums} ? {sol.canJump(nums)}")
    nums2 = [3,2,1,0,4]
    print(f"Can jump to the last index in the array {nums2} ? {sol.canJump(nums2)}")

if __name__ == "__main__":
    main()