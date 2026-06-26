class Solution:
    def maxProfit(self, prices: list[int]) -> int:    
        highMargin = 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                highMargin += (prices[i] - prices[i-1])
        return highMargin
                    

prices = [7,1,5,3,6,4]
worker = Solution()
ans1 = worker.maxProfit(prices)
print(ans1)

#Best Time to Buy and Sell Stock II