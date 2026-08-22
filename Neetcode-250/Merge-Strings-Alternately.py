class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:       
        l1,l2 = 0,0
        merged_words = []
        while l1 < len(word1) and l2 < len(word2):
            merged_words.append(word1[l1])
            merged_words.append(word2[l2])
            l1,l2 = l1+1, l2+1
        merged_words.append(word1[l1:])
        merged_words.append(word2[l2:])
        return "".join(merged_words)



word1 = "ab"
word2 = "pqrs"
worker = Solution()
ans1 = worker.mergeAlternately(word1,word2)
print(ans1)

#Merge Strings Alternately