class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longS = 0
        window = dict()
        l = 0
        maxF = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r],0)
            maxF = max(maxF,window[s[r]])
            while (r-l+1) - maxF > k:
                window[s[l]] -= 1
                l += 1
            longS = max(longS, r-l+1)
        return longS
        

s = "AABABBA"
k = 1
worker = Solution()
ans1 = worker.characterReplacement(s,k)
print(ans1)

#Longest Repeating Character Replacement