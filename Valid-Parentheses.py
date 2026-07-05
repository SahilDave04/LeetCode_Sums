class Solution:
    def isValid(self, s: str) -> bool:
        combs = {")":"(","}":"{","]":"["}
        stack = list()

        for l in s:
            if l in combs.keys():
                if stack and combs[l] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(l)             
        return True if not stack else False


s = "{}"
worker = Solution()
ans1 = worker.isValid(s)
print(ans1)

#Valid Parentheses