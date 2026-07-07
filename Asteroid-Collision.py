class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        cola = list()
        for a in asteroids:
            while cola and a < 0 and cola[-1] > 0:
                diff = cola[-1] + a
                if diff < 0:
                    cola.pop()
                elif diff > 0:
                    a = 0
                else:
                    a = 0
                    cola.pop()
            if a:
                cola.append(a)
        return cola


asteroids = [3,5,-6,2,-3,4]
worker = Solution()
ans1 = worker.asteroidCollision(asteroids)
print(ans1)

#Asteroid Collision