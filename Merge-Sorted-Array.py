class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        last = m+n-1
        print(last)
        while m > 0 and n > 0:
            if nums1[m-1] < nums2[n-1]:
                nums1[last] = nums2[n-1]
                n -= 1
            else:
                nums1[last] = nums1[m-1]
                m -= 1
            last -= 1
            print(nums1,m,n,last)
        
        while n > 0:
            nums1[last] = nums2[n-1]
            n -= 1
            last -= 1
        print(nums1)




nums1 = [2,2,3,0,0,0,0]
m = 3
nums2 = [1,1,5,6]
n = 4
worker = Solution()
ans1 = worker.merge(nums1,m,nums2,n)
print(ans1)

#Merge Sorted Array