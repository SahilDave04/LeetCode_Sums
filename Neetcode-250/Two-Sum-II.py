class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l,r = 0, len(numbers)-1

        while l != r:
            added = numbers[l] + numbers[r]
            if added > target:
                    r -= 1
            elif added < target:
                l += 1
            else:
                return [l+1,r+1]
                

numbers = [3,24,50,79,88,150,345]
target = 200
worker = Solution()
ans1 = worker.twoSum(numbers,target)
print(ans1)

#Two Sum II