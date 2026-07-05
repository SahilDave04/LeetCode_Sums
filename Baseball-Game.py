class Solution:
    def calPoints(self, operations: list[str]) -> int:
        scores = list()
        for op in range(len(operations)):
            if operations[op] == "+":
                scores.append(scores[-1]+scores[-2])
            elif operations[op] == "D":
                scores.append(2*scores[-1])
            elif operations[op] == "C":
                scores.pop()
            else:
                scores.append(int(operations[op]))
        return sum(scores)


ops = ["5","2","C","D","+"]
worker = Solution()
ans1 = worker.calPoints(ops)
print(ans1)

#Baseball Game