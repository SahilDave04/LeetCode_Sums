def jump(nums):
    goal = len(nums)-1
    cache = []
    total = 0
    def worker(nums):
        temp = []
        for i in nums:
            if total != goal:
                sum += i
                temp.append()
            else:
                break

    
nums = [2,3,1,1,4]
ways = jump(nums)
print(ways)