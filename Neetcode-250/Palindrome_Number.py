#Given an integer x, return true if x is a palindrome, and false otherwise

import numpy as np
x = 1001
breaks = [*str(x)]
sz = len(breaks)
#print(sz)
if sz%2 == 0:
        if sz == 2:
                if breaks[0] != breaks[1]:
                        deci = False
                else:
                        deci = True
        #print("even")
        else:
                l1 = int((sz/2)-1)
                l2 = int((sz/2))
                trs = []
                i = 0
                ek = len(trs)
                while ek != int(sz/2):
                        #print(l1,l2)
                        #print(breaks[l1],breaks[l2])
                        if breaks[l1-i] != breaks[l2+i]:
                                trs.append(1)
                                break
                        else:
                                trs.append(0)
                        ek = len(trs)
                        i += 1
                if len(trs) != int(sz/2):
                        deci = False
                else:
                        deci = True
                #print(deci)

else:
        #print("odd")
        if sz == 1:
                deci = True
        else:
                mid = int((sz-1)/2)
                #print(mid)
                trs = []
                i = 1
                while len(trs) != mid:
                        #print(breaks[mid+i] == breaks[mid-i])
                        if breaks[mid+i] != breaks[mid-i]:
                                trs.append(1)
                                break
                        else:
                                trs.append(0)
                        i += 1
                #print(trs)
                if len(trs) != mid:
                        deci = False
                else:
                        pick = np.zeros((1,mid),dtype=int)
                        #print(pick)
                        if trs != list(pick[0]):
                                deci = False
                        else:
                                deci = True
print(deci)
