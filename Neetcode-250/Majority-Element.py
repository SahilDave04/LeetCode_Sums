class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count, res = 0,0
        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res
                    

nums = [3,2,3]
worker = Solution()
ans1 = worker.majorityElement(nums)
print(ans1)

#Majority Element