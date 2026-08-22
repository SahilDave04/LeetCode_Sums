def isSubsequence(s,t):
    flags = []
    latest = 0
    for l in s:
        for i in range(latest,len(t)):
            print(t[i],l)
            if t[i] == l:
                latest = i+1
                flags.append(1)
                break
    if flags == [1]*len(s):
        return True
    else:
        return False

s = 'aza'
t = 'abzba'
verdict = isSubsequence(s,t)
print(verdict)