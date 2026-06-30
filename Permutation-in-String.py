class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        comp = dict()
        window = dict()
        l = 0
        for i in s1:
            comp[i] = 1 + comp.get(i,0)
        for r in range(len(s2)):
            if r-l+1 > len(s1):
                if window[s2[l]] == 1:
                    del window[s2[l]]
                else:
                    window[s2[l]] -= 1
                l += 1
            window[s2[r]] = 1 + window.get(s2[r],0)
            r += 1
            if window == comp:
                return True
        return False

s1 = "ab"
s2 = "eidbaooo"
worker = Solution()
ans1 = worker.checkInclusion(s1,s2)
print(ans1)

#Permutation in String