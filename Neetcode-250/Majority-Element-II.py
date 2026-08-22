class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        majority = len(nums)//3
        majors = list()
        counts = dict()
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
            if counts[num] > majority and num not in majors:
                majors.append(num)
        return majors
                    

nums = [1,2]
worker = Solution()
ans1 = worker.majorityElement(nums)
print(ans1)

#Majority Element II