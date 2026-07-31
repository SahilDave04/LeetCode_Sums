import math

class MountainArray:
    def __init__(self,mountainArr):
        self.mountainArr = mountainArr

    def get(self, index: int) -> int:
        return self.mountainArr[index]

    def length(self) -> int:
        return len(self.mountainArr)

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        l,r = 1,mountainArr.length()-2
        count = 1

        #Finding Peak
        while True:
            m = (l+r)//2
            mVal = mountainArr.get(m)
            nextM = mountainArr.get(m+1)
            if mVal < nextM:
                l = m + 1
            elif mVal > nextM:
                if mVal > mountainArr.get(m-1):
                    break
                r = m - 1
            count += 2
        
        #Binary Search on Left Side
        l,r = 0,m
        res = -1
        while l <= r:
            m = (l+r)//2
            mVal = mountainArr.get(m)
            count += 1
            #print(res)
            if target < mVal:
                r = m -1
            elif target > mVal:
                l = m + 1
            else:
                print(count)
                return m

        #Binary Search on Right Side
        l,r = m+1,mountainArr.length()-1      
        while l <= r:
            m = (l+r)//2
            mVal = mountainArr.get(m)   
            count += 1
            #print(res)
            if target > mVal:
                r = m -1
            elif target < mVal:
                l = m + 1
            else:
                print(count)
                return m
        print(count)
        return -1

      
mountainArr = [1,2,3,4,5,3,1]
target = 3
mountain = MountainArray(mountainArr)
worker = Solution()
ans1 = worker.findInMountainArray(target,mountain)
print(ans1)

#Find in Mountain Array