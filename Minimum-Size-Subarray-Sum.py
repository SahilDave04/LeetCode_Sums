class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l, total = 0, 0
        minS = len(nums)+1

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                minS = min(minS,r-l+1)
                total -= nums[l]
                l += 1
        return 0 if minS == len(nums)+1 else minS
        

target = 7
nums = [2,3,1,2,4,3]
worker = Solution()
ans1 = worker.minSubArrayLen(target,nums)
print(ans1)

#Minimum Size Subarray Sum