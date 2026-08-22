class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pos_spd = [[p,s] for p,s in zip(position,speed)]
        stack = list()
        for p,s in sorted(pos_spd)[::-1]:
            stack.append((target-p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
            print(stack)
            print(p,s)
        return len(stack)


target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
worker = Solution()
ans1 = worker.carFleet(target,position,speed)
print(ans1)

#Car Fleet (Important Question)