class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        window,tC = dict(),dict()

        for j in t:
            tC[j] = 1 + tC.get(j,0)

        have,need = 0,len(tC)
        minS ,minL = [-1,-1], len(s)+1
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in tC and window[c] == tC[c]:
                have += 1

            while have == need:
                if (r-l+1) < minL:
                    minS = [l,r]
                    minL = r-l+1
                window[s[l]] -= 1
                if s[l] in tC and window[s[l]] < tC[s[l]]:
                    have -= 1
                l += 1
        l,r = minS
        return s[l:r+1] if minL != len(s)+1 else ""
        
                        
s = "ADOBECODEBANC"
t = "ABC"
worker = Solution()
ans1 = worker.minWindow(s,t)
print(ans1)

#Minimum Window Substring (important question)