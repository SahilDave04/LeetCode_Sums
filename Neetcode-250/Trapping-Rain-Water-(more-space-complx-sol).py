class Solution:
    def trap(self, height: list[int]) -> int:
        maxLeft = [height[0]]
        maxRight = [height[len(height)-1]]
        water = 0
        for i in range(1,len(height)):
            if height[i] > maxLeft[i-1]:
                maxLeft.append(height[i])
            else:
                maxLeft.append(maxLeft[i-1])

            if height[len(height)-1-i] > maxRight[i-1]:
                maxRight.append(height[len(height)-1-i])
            else:
                maxRight.append(maxRight[i-1])
        maxRight = maxRight[::-1]
        print(maxLeft,maxRight)
        mins = [min(maxLeft[j],maxRight[j]) for j in range(len(height))]
        print(mins)
        for k in range(len(height)):
            sub = mins[k] - height[k]
            if sub > 0:
                water += sub
        return water

                

            
height = [0,1,0,2,1,0,1,3,2,1,2,1]
worker = Solution()
ans1 = worker.trap(height)
print(ans1)

#Trapping Rain Water (more space complx sol)