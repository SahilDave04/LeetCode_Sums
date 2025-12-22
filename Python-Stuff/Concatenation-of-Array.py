'''
Problem Link - https://leetcode.com/problems/concatenation-of-array/description/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
'''

def getConcatenation(nums: list[int]) -> list[int]:
        return nums+nums

nums = [1,2,1]
op = getConcatenation(nums)
print(op)