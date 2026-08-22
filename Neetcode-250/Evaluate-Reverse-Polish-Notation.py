import math

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        def process(n1,n2,op):
            if op == "+":
                return n1+n2
            elif op == "-":
                return n1-n2
            elif op == "*":
                return n1*n2
            else:
                return math.trunc(n1/n2)
        
        ops = "+-*/"
        nums = list()
        for r in range(len(tokens)):
            if tokens[r] in ops:
                n2 = nums.pop()
                n1 = nums.pop()
                opt = process(n1,n2,tokens[r])
                nums.append(opt)
            else:
                nums.append(int(tokens[r]))
            print()
        return nums[0]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
worker = Solution()
ans1 = worker.evalRPN(tokens)
print(ans1)

#Evaluate Reverse Polish Notation