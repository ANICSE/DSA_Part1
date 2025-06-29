from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        #Brute-Force O(n^2)
        for i in range(len(nums)):
            for j in range((i+1), len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
    
    def two_sumHashMap(self, nums: List[int], target: int)-> List[int]:
        #Optimized Approach Hash Map: O(n)
        prevMap = {} #value: index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return []

def main():
    sol = Solution()
    nums = [2, 7, 11, 5]
    target = 7
    print("Solution using brute force")
    print(f"Target {target} present in the indices of array {nums}: {sol.two_sum(nums, target)}")

    print("Solution using HashMap")
    print(f"Target {target} present in the indices of array {nums}: {sol.two_sum(nums, target)}")

if __name__ == "__main__":
    main()