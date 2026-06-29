class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()
        l = 0
        for r in range(len(nums)):
            if r-l > k:
                window.remove(nums[l])
                l += 1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False

                

            
nums = [1,0,1,1]
k = 1
worker = Solution()
ans1 = worker.containsNearbyDuplicate(nums,k)
print(ans1)

#Contains Duplicate II (sliding window)