import math

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l,r = max(weights),sum(weights)
        res = r

        def ships(cap):
            temp = 0
            ds = 1
            for w in weights:
                diff = m - temp
                if w > diff:
                    ds += 1
                    temp = 0                   
                temp += w
            return ds

        while l <= r:
            m = (l+r)//2
            if ships(m) > days:
                l = m + 1
            else:
                r = m - 1
                res = min(res,m)
        return res


weights = [10,50,100,100,50,100,100,100]
days = 5
worker = Solution()
ans1 = worker.shipWithinDays(weights,days)
print(ans1)

#Capacity To Ship Packages Within D Days