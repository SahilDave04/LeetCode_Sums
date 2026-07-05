import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        l,r = 0,0
        mdq = collections.deque()
        mxs = list()

        while r < len(nums):
            while mdq and nums[mdq[-1]] < nums[r]:
                mdq.pop()
            mdq.append(r)

            if l > mdq[0]:
                mdq.popleft()

            if (r+1) >= k:
                mxs.append(nums[mdq[0]])
                l += 1
            r += 1
            #print(l,r,mdq)
        return mxs
                        
nums = [1,3,-1,-3,5,3,6,7]
k = 3
worker = Solution()
ans1 = worker.maxSlidingWindow(nums,k)
print(ans1)

#Sliding Window Maximum (important question)