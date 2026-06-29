class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subL = 0
        l= 0
        window = set()
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l += 1
            window.add(s[r])
            subL = max(subL,r-l+1)
        return subL
            
s = "pwwkew"
worker = Solution()
ans1 = worker.lengthOfLongestSubstring(s)
print(ans1)

#Longest Substring Without Repeating Characters