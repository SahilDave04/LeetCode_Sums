class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = [] # contains (index,height)

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                maxArea = max(maxArea,(height*(i - index)))
                start = index
            stack.append((start,h))
        
        for i,h in stack:
            maxArea = max(maxArea,h*(len(heights) - i))

        return maxArea

heights = [2,1,5,6,2,3]
worker = Solution()
ans1 = worker.largestRectangleArea(heights)
print(ans1)
#Largest Rectangle in Histogram (Important Question)