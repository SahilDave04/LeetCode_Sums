import math
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A,B = nums1,nums2

        if len(B) < len(A):
            A,B = B,A

        # A is always the shorter

        total = len(A)+len(B)
        half = total//2

        l,r = 0,len(A)-1
        while True:
            i = (l+r)//2
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if i+1 < len(A) else float("infinity") 

            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            #print(Aleft,Aright,Bleft,Bright)

            if Aleft <= Bright and Bleft <= Aright:
                #print("here")
                #even
                if total%2 == 0:
                    return ( max(Aleft,Bleft) + min(Aright,Bright) )/2
                
                #odd
                return min(Aright,Bright)

            elif Aleft > Bright:
                r  = i - 1
            else:
                l = i + 1

       
nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10,11,12,13,14,15,16,17]
worker = Solution()
ans1 = worker.findMedianSortedArrays(nums1,nums2)
print(ans1)

#Median of Two Sorted Arrays (Very Important Question)