class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        prof = []
        for i in range(len(prices)-1):
            curry = prices[i]
            cutout = max([val-curry for val in prices[i+1:]])
            print(cutout)
            if cutout > 0:
                prof.append(cutout)
        print(prof)
        if prof == []:
            return 0
        else:
            maxProf = max(prof)
            return maxProf
    
prices = [7,6,4,3,1]
profit = Solution().maxProfit(prices)
print(profit)