import numpy as np
nums = [1,2,3,4]
pds = []
wks = []
uns = list(np.unique(np.array(nums)))
#print(uns)
if 0 in uns:
        z_cnt = nums.count(0)
        #print(z_cnt)
        if z_cnt > 1:
                pds = list(np.zeros((1,len(nums)),dtype=int)[0])
        else:
                lp = nums.copy()
                lp.remove(0)
                prd = np.prod(lp)
                #print(prd)
                for j in nums:
                        if j == 0:
                                pds.append(prd)
                        else:
                                pds.append(0)
else:
        for b in uns:
                cnt = nums.count(b)
                prdct = b**cnt
                wks.append(prdct)
        #print(wks)
        tot = np.prod(wks)
        #print(tot)
        vls = []
        for i in uns:
                vls.append(int(tot/i))
        #print(vls)
        alcs = dict(zip(uns,vls))
        #print(alcs)
        for l in nums:
                pds.append(alcs[l])
print(pds)
