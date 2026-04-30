class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefixSums = {0:1}
        res = 0
        running_sum = 0
        for i in nums:
            running_sum += i
            diff = running_sum - k
            res += prefixSums.get(diff,0)
            prefixSums[running_sum] = 1 + prefixSums.get(running_sum,0)
        return res


nums = [1,-1,1]
k = 0
worker = Solution()
ans1 = worker.subarraySum(nums,k)
print(ans1)

#Subarray Sum Equals K