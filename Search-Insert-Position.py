class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m
        return l

nums = [1,3,5,6]
target = 7
worker = Solution()
ans1 = worker.searchInsert(nums,target)
print(ans1)

#Search Insert Position