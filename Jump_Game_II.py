from typing import List
class Solution:
    def canJUmpMIN(self, nums: List[int])-> int:
        res = 0
        l = r = 0

        while r < len(nums)-1:
            farthest = 0
            for i in range(l, r+1):
                farthest = max(farthest, i+nums[i])
            
            l = r+1
            r = farthest
            res+=1
        
        return res

def main():
    sol = Solution()
    nums = [2,3,1,1,2, 1, 6]
    print(f"Nuber of jumps: {sol.canJUmpMIN(nums)}")

if __name__ == "__main__":
    main()