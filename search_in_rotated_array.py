from typing import List

class Solution:
    def search(self, nums: List[int], target):
        l, r = 0, len(nums)-1        

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            #process left ortion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid -1
            #process right portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid -1
                else:
                    l = mid + 1
        
        return -1

def main():
    sol = Solution()
    nums = [4, 5, 6, 7,0, 1,2]
    target = 4

    print(f"target {target} present in index for list of array {nums}: {sol.search(nums, target)}")
        

if __name__ == "__main__":
    main()