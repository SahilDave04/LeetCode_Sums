class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        sub = ""

        # If the path doesn't end with "/"
        if path[-1] != "/":
            path += "/"
        
        # Going through each character
        for l in path:
            if l == "/":
                if sub == "..":
                    if stack: stack.pop()
                elif sub != "" and sub != ".":
                    stack.append(sub)
                sub = ""
            else:
                sub += l
        return f"/{"/".join(stack)}"

path = "/a/../../b/../c//.//"
worker = Solution()
ans1 = worker.simplifyPath(path)
print(ans1)

#Simplify Path