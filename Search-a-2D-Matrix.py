class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        t,b = 0,len(matrix)-1
        while t <= b:
            mid = t+((b-t)//2)
            if matrix[mid][0] > target:
                b = mid - 1
            elif matrix[mid][0] < target:
                t = mid + 1
            else:
                return True

        l,r = 0,len(matrix[b])-1
        while l <= r:
            mid = l + ((r-l)//2)
            if matrix[b][mid] > target:
                r = mid - 1
            elif matrix[b][mid] < target:
                l = mid + 1
            else:
                return True
        return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 11
worker = Solution()
ans1 = worker.searchMatrix(matrix,target)
print(ans1)

#Search a 2D Matrix