from typing import List

class Solution:
    def house_robber_II(self, nums: List[int])-> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) #nums[1:]->skip first number, nums[:-1]->skip last number


    def helper(self, nums):
        rob1, rob2 =0, 0
        for n in nums:
            newRob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = newRob
        return rob2
    
def main():
    sol = Solution()
    nums = [1, 2, 3, 1, 4]
    print(f"Maximum roberry in {nums}----> {sol.house_robber_II(nums)}")

if __name__ =="__main__":
    main()