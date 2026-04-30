class Solution:
    def reverseString(self, s: list[int]) -> int:
        stack = []
        for i in s:
            stack.append(i)

        l = 0
        while stack:
            s[l] = stack.pop()
            l+=1
        return s


s = ["h","e","l","l","o"]
worker = Solution()
ans1 = worker.reverseString(s)
print(ans1)

#Reverse String (stack solution)