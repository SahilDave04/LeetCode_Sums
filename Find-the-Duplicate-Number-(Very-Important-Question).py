class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        # Floyd's Cycle Detection (watch video again)
        # Slow Pointer (one step), Fast Pointer (two steps)

        slow1, fast = 0,0
        while True:
            slow1 = nums[slow1]
            fast = nums[nums[fast]]
            if slow1 == fast:
                break

        slow2 = 0
        while True:
            slow1 = nums[slow1]
            slow2 = nums[slow2]
            if slow1 == slow2:
                return slow1
        
                
nums = [1,3,4,3,2]
worker = Solution()
ans1 = worker.findDuplicate((nums))
print(ans1)

#Find the Duplicate Number (Very Important Question)