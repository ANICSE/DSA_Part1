from typing import List
class Solution:
    def maxScore(self, nums: List[int], x: int)->int:
        # dp0: max score if last visited node even
        # dp1: max score if last visited node odd
        dp0 = dp1 = float('-inf')

        if nums[0] % 2 == 0:
            dp0 = nums[0]
        else:
            dp1 = nums[0]

        for v in  nums[1:]:
            parity = v%2
            if parity == 0:
                dp0 = max(dp0+v, dp1+v-x)
            else:
                dp1 = max(dp1+v, dp0+v-x)
        
        return max(dp0, dp1)

def main():
    sol = Solution()
    nums = [2,3,6,1,9,2]
    x = 5
    print(f"MAximum score possible in the array od integers {nums} is: {sol.maxScore(nums, x)}")

if __name__ == "__main__":
    main()