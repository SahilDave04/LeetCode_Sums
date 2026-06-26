def gcd(xi,mxi):
    latest_rem = None
    if xi == mxi:
        return xi
    else:
        if xi != 0:
            latest_rem = mxi%xi
            print(latest_rem)
            return gcd(latest_rem,xi)

def gcdSum(nums):
    #prefixGcd = [lambda arg=i: ]
    pass

nums = [2,6,4]
#summit = gcdSum(nums)
print(gcd(192,270))