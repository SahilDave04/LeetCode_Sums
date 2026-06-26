class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        s, e = 0, 1

        while e != len(nums):
            if nums[e] != nums[s]:
                nums[s+1] = nums[e]
                s += 1
            e += 1
        return s+1,nums



nums = [1,2,2,5,6,6,7,9,9]
worker = Solution()
ans1 = worker.removeDuplicates(nums)
print(ans1)

#Remove Duplicates from Sorted Array