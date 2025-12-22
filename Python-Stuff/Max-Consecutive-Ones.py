'''
Problem Link - https://leetcode.com/problems/max-consecutive-ones/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
'''

def findMaxConsecutiveOnes(nums: list[int]) -> int:
        count = 0
        high = 0
        for i in nums:
            if i == 1: 
                count += 1
                if count > high:
                    high = count
            else: count = 0
        return high

nums = [1,1,0,1,1,1]
op = findMaxConsecutiveOnes(nums)
print(op)