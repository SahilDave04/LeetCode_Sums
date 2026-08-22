from collections import defaultdict

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1
            if len(counts) <= 2:
                continue
            new_counts = defaultdict(int)
            for k,v in counts.items():
                if v > 1:
                    new_counts[k] = v-1
            counts = new_counts
        res = []
        for i in counts:
            if nums.count(i) > len(nums)//3:
                res.append(i)
        return res

                    

nums = [1,2,4,1,2,1,2,1,4]
worker = Solution()
ans1 = worker.majorityElement(nums)
print(ans1)

#Majority Element II (Approach 2)