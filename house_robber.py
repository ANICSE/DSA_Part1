from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[1]

        v1, v2 = nums[0], max(nums[0], nums[1])
        for i in range(2, n):
            tmp = v2
            v2 = max(v2, v1 + nums[i])
            v1 = tmp
        return v2
    
    def rob_v1(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        #[rob1, rob2, n, n+1,..]
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 =temp
        return rob2

def main():
    sol = Solution()
    nums = [2, 7, 9, 3, 1]
    print(f"Max Rob {sol.rob(nums)}")
    print(f"Max Rob Version1 {sol.rob_v1(nums)}")

if __name__ == "__main__":
    main()