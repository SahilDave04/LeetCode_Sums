class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = list()
        ans = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                sTemp,sInd = stack.pop()
                ans[sInd] = i - sInd
            stack.append([t,i])
        return ans


temperatures = [73,74,75,71,69,72,76,73]
worker = Solution()
ans1 = worker.dailyTemperatures(temperatures)
print(ans1)

#Daily Temperatures