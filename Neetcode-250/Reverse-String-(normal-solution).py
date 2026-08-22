class Solution:
    def reverseString(self, s: list[int]) -> int:
        temp = None
        l = 0
        r = len(s)-1
        while r > l:
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1
            r -= 1
        return s


s = ["h","e","l","l","o"]
worker = Solution()
ans1 = worker.reverseString(s)
print(ans1)

#Reverse String (normal solution)