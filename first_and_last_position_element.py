from typing import List
class Solution:
    def binsearch(self, nums: List[int], target: int)-> List[int]:
        left = self.search(nums, target, True)
        right = self.search(nums, target, False)
    
        return [left, right]

    def search(self, nums, target, leftbias):
        l, r = 0, len(nums)-1
        i = -1
        while l <=r:
            mid = (l+r)//2
            if target > nums[mid]:
                l =mid+1
            elif target < nums[mid]:
                r = mid -1
            else:
                i = mid
                if leftbias: # Continue search in left if more target is there
                    r = mid -1
                else: #continue search in right if more target is there
                    l = mid +1
                
        return i

def main():
    sol = Solution()
    nums = [5, 7, 7, 8, 8, 8, 10, 11]
    target = 7
    print(f"target {target} in array {nums} present in range -> {sol.binsearch(nums, target)}")

if __name__ == "__main__":
    main()