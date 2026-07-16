class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0,x
        res = 0
        while l <= r:
            m = (l+r)//2
            if x > m**2:
                l = m + 1
                res = m
            elif x < m**2:
                r = m - 1
            else:
                return m                
        return res
            

x = 1
worker = Solution()
ans1 = worker.mySqrt(x)
print(ans1)

#Sqrt(x) (Important Question)