class Solution:
    def findMin(self, nums: list[int]) -> int:
        l,r = 0,len(nums)-1
        res = nums[0]       

        while l <= r:
            if nums[r] > nums[l]:
                res = min(res,nums[l])
                break

            m = (l+r)//2
            res = min(res,nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res


nums = [2,1]
worker = Solution()
ans1 = worker.findMin(nums)
print(ans1)

#Find Minimum in Rotated Sorted Array