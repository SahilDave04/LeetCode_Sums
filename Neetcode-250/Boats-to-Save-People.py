class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        minBoats = 0
        l,r = 0,len(people)-1
        people.sort()
        while l <= r:
            remain = limit - people[r]
            r -= 1
            minBoats += 1
            if l <= r and people[l] <= remain:
                l += 1
        return minBoats
            
people = [1,2,2]
limit = 3
worker = Solution()
ans1 = worker.numRescueBoats(people,limit)
print(ans1)

#Boats to Save People