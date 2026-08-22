'''Problem Link - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/?envType=problem-list-v2&envId=dsa-linear-shoal-array-ii'''


def smallerNumbersThanCurrent(nums):
    cnts = []
    for i in nums:
        temps = [j for j in nums if j < i]
        cnt = len(temps)
        cnts.append(cnt)
    print(cnts)
    return cnts
 
nums = [7,7,7,7]
smallerNumbersThanCurrent(nums)