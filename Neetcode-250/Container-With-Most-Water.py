class Solution:
    def maxArea(self, height: list[int]) -> int:
        l,r = 0,len(height)-1
        maxWater = 0
        while l < r:
            area = min(height[l],height[r])*(r-l)
            if area > maxWater:
                maxWater = area
            print(area,l,r,maxWater)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return maxWater
            
            
height = [1,8,6,2,5,4,8,3,7]
worker = Solution()
ans1 = worker.maxArea(height)
print(ans1)

#Container With Most Water