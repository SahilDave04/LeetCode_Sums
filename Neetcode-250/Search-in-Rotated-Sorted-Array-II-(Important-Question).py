class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l,r = 0, len(nums)-1

        while l <= r:
            m = (r+l)//2
            if target == nums[m]: return True
            if nums[m] > nums[l]:
                if nums[m] > target >= nums[l]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] < nums[l]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1
        return False


nums = [2,5,6,0,0,1,2]
target = 0
worker = Solution()
ans1 = worker.search(nums,target)
print(ans1)

#Search in Rotated Sorted Array II (Important Question)