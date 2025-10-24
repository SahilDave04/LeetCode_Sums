def rome(s):
    values = {"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    specials = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
    skipper = False
    tot = 0
    for i in range(len(s)-1,-1,-1):
        #print(skipper)
        if skipper == False:
            cur = s[i]
            print(f'>{cur}')
            if i != 0:
                left = s[i-1]
                combo = left+cur
            else:
                left = None
                combo = cur

            if combo in specials:
                #print("c1")
                skipper = True
                val = specials[combo]
            else:
                val = values[cur]
                #print("c2")
                skipper = False
            tot = tot + val
        else:
            #print("here")
            skipper = False

    return tot


string = "MCMXCIV"
number = rome(string)