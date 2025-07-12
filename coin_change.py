from typing import List
class Solution:
    def coin_change(self, coins: List[int], amount: int)->int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount+1):
            for c in coins:
                if a - c >=0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
    
def main():
    sol = Solution()
    nums = [1,2,5]
    amount = 11

    print(f"Minimum number of coins in {nums} to get {amount} is {sol.coin_change(nums, amount)}")

if __name__ == "__main__":
    main()