from typing import List
class Solution:
    def buy_n_sell(self, stocks: List[int]) -> int:
        left, right = 0, 1
        maxProfit = 0

        while right < len(stocks):
            if stocks[left] < stocks[right]:
                profit = stocks[right] - stocks[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            
            right+= 1
        
        return maxProfit
    
def main():
    sol = Solution()
    stocks = [7, 1, 5, 3, 8, 4]
    print(f"Maximum profit for stock prics {stocks} is : {sol.buy_n_sell(stocks)}")

if __name__ == "__main__":
    main()