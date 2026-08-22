class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mProfit = 0
        l,r = 0,1
        while r < len(prices):
            if prices[l] > prices[r]:
                l= r
            else:
                mProfit = max(mProfit,prices[r]-prices[l])
            r += 1
        return mProfit
            
prices = [7,1,5,3,6,4]
worker = Solution()
ans1 = worker.maxProfit(prices)
print(ans1)

#Best Time to Buy and Sell Stock