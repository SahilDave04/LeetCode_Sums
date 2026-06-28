class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        def helper(l,r):
            while l < r:
                nums[l],nums[r] = nums[r],nums[l]
                l,r = l+1, r-1
            return nums

        k = k%len(nums)
        nums = helper(0,len(nums)-1)
        nums = helper(0,k-1)
        nums = helper(k,len(nums)-1)
                    
            
nums = [1,2,3,4,5,6,7]
k = 3
worker = Solution()
ans1 = worker.rotate(nums,k)
print(ans1)

#Rotate Array