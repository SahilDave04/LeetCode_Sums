class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        l,r = 0,len(arr)-k

        while l < r:
            m = (l+r)//2
            if x-arr[m] > arr[m+k] - x:
                l = m + 1
            else:
                r = m
            print(l,r,m,arr[l:l+k])
        return arr[l:l+k]


arr = [1,1,2,3,4,5]
k = 4
x = -1
worker = Solution()
ans1 = worker.findClosestElements(arr,k,x)
print(ans1)

#Find K Closest Elements (neetcode sliding window)