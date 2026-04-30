class Solution:
    def reverseString(self, s: list[int]) -> int:
        def reverse(s,l,r):
            if l < r:
                s[l],s[r] = s[r],s[l]
                reverse(s,l+1,r-1)
            return s
        reverse(s,0,len(s)-1)
        return s


s = ["h","e","l","l","o"]
worker = Solution()
ans1 = worker.reverseString(s)
print(ans1)

#Reverse String (recursion solution)