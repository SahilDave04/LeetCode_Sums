'''
Problem Link - https://leetcode.com/problems/shuffle-the-array/?envType=problem-list-v2&envId=dsa-linear-shoal-array-i
'''

def shuffle(nums: list[int], n: int) -> list[int]:
        new_nums = list()
        for i in range(n):
            new_nums.append(nums[i])
            new_nums.append(nums[i+n])
        return new_nums

nums = [2,5,1,3,4,7]
n = 3
op = shuffle(nums,n)
print(op)