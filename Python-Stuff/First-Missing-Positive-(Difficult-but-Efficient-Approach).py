class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        for j in range(len(nums)):
            val = abs(nums[j])
            print(nums[j],val)
            if 1 <= val <= len(nums):
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -1*(len(nums)+1)

        for k in range(1,len(nums)+1):
            if nums[k-1] >= 0:
                return k

        return len(nums)+1


nums = [3,4,-1,1]
worker = Solution()
ans1 = worker.firstMissingPositive(nums)
print(ans1)

#First Missing Positive (Difficult but Efficient Approach)