class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        there = set()
        for i in nums:
            if i not in there:
                there.add(i)
        for n in range(1,len(nums)+1):
            if n not in there:
                return n
        return len(nums)+1


nums = [1]
worker = Solution()
ans1 = worker.firstMissingPositive(nums)
print(ans1)

#First Missing Positive