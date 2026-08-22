class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def breaking(largest):
            tempSum = 0
            subs = 0

            for n in nums:
                tempSum += n
                if tempSum > largest:
                    tempSum = n
                    subs += 1

            return subs+1 <= k

        l,r = max(nums),sum(nums)
        res = r
        while l <= r:
            m = l + ((r-l)//2)
            if breaking(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res



        
nums = [1,2,3,4,5]
k = 3
worker = Solution()
ans1 = worker.splitArray(nums,k)
print(ans1)

#Split Array Largest Sum (Very Important Question)