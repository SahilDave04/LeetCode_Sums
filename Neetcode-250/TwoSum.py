#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input 
#would have exactly one solution, and you may not use the same element twice.

nums = [2,7,11,15]
target = 9

inds = []
ds = False
for i in range(0,len(nums)):
        p1 = nums[i]
        diff = target - p1
        if diff in nums:
                ids = nums.index(diff)
                if ids != i:
                        inds.append(i)
                        inds.append(ids)
                        break
print(inds)
