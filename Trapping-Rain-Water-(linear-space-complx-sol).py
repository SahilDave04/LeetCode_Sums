class Solution:
    def trap(self, height: list[int]) -> int:
        l,r = 0,len(height)-1
        maxLeft = height[l]
        maxRight = height[r]
        water = 0
        while l < r:
            if maxRight < maxLeft:
                sub = maxRight - height[r]
                r -= 1
                maxRight = max(height[r],maxRight)
            else:
                sub = maxLeft - height[l]
                l += 1
                maxLeft = max(height[l],maxLeft)

            if sub > 0:
                    water += sub        

        return water

                

            
height = [5,5,1,7,1,1,5,2,7,6]
worker = Solution()
ans1 = worker.trap(height)
print(ans1)

#Trapping Rain Water (linear space complx sol)