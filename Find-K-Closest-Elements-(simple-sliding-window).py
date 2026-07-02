class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l,r = 0,len(arr)-1

        while r-l+1 > k:
            while x-arr[l] <= arr[r]-x and r-l+1 > k:
                r -= 1
            while x-arr[l] > arr[r]-x and r-l+1 > k:
                l += 1
        return arr[l:r+1]


arr = [1,2,3,4,5]
k = 4
x = 3
worker = Solution()
ans1 = worker.findClosestElements(arr,k,x)
print(ans1)

#Find K Closest Elements (simple sliding window)