class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        trips = list()
        nums.sort()
        
        # Here we are sorting the array first and then solving the problem
        # Time Complexity - O(nlogn)+O(n^2)

        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l,r = i+1,len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    trips.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return trips


nums = [-1,0,1,2,-1,-4]
worker = Solution()
ans1 = worker.threeSum(nums)
print(ans1)

#3Sum