'''
Problem Link - https://leetcode.com/problems/set-mismatch/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii
'''

def findErrorNums(nums: list[int]) -> list[int]:
        n = len(nums)
        see = [nums.count(i) for i in range(1,n+1)]
        out = [see.index(2)+1,see.index(0)+1]
        return out

nums = [1,2,2,4]
op = findErrorNums(nums)
print(op)

