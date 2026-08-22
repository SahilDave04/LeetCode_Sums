class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
                
        for r in s:
            if r == "]":
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num)*sub)
            else:
                stack.append(r)
        return "".join(stack)


s = "2[abc]3[cd]ef"
worker = Solution()
ans1 = worker.decodeString(s)
print(ans1)

#Decode String