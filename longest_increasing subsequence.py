from typing import List
import bisect
class Solution:
    def LIS(self, nums: List[int])->int:
        #nums.sort()
        dp = []
        for i in nums:
            idx = bisect.bisect_left(dp, i)
            if idx == len(dp):
                dp.append(i)
            else:
                dp[idx] = i
        return len(dp)
        
def main():
    sol = Solution()
    #nums = [0,1,0,3,2,3]
    #nums = [10,9,2,5,3,7,101,18]
    nums = [7,7,7,7,7]
    print(f"The LIS of {nums} is : {sol.LIS(nums)}")

if __name__ == "__main__":
    main()