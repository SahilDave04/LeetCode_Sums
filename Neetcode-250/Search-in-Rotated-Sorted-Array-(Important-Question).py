class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            m = (r+l)//2
            if target == nums[m]: return m
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1


nums = [4,5,6,7,0,1,2]
target = 1
worker = Solution()
ans1 = worker.search(nums,target)
print(ans1)

#Search in Rotated Sorted Array (Important Question)