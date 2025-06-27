from typing import List
class Solution:
    def cotainsDuplicate(self, nums: List[int], k: int, t: int)-> bool:
        n = len(nums)
        if t == 0 and n == len(set(nums)):
            return False
        
        for i in range(n):
            for j in range(i+1, i+1+k):
                if j>=n:
                    break
                if abs(nums[i] - nums[j]) <=t:
                    return True
        return False
    
def main():
    sol = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    t = 0
    print(f"Test 1: {sol.cotainsDuplicate(nums, k, t)}")  # Expected: True

    nums2 = [1, 5, 9, 1, 5, 9]
    k2 = 2
    t2 = 3
    print(f"Test 2: {sol.cotainsDuplicate(nums2, k2, t2)}")  # Expected: False

    nums3 = [1, 0, 1, 1]
    k3 = 1
    t3 = 2
    print(f"Test 3: {sol.cotainsDuplicate(nums3, k3, t3)}")  # Expected: True

if __name__ == "__main__":
    main()