word1 = "ab"
word2 = "pq"
new = ""
if len(word1) > len(word2):
        for i in range(0,len(word2)):
                p1 = ""
                l1 = word1[i]
                l2 = word2[i]
                p1 = l1+l2
                new = new + p1
        remain = word1[len(word2):len(word1)]
        new = new + remain
else:
        for i in range(0,len(word1)):
                p1 = ""
                l1 = word1[i]
                l2 = word2[i]
                p1 = l1+l2
                new = new + p1
        remain = word2[len(word1):len(word2)]
        new = new + remain

print(new)
