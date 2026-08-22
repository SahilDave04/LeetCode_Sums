def countCommas(n):
    for num in range(1,n+1):
        coma_step = 3
        size = len(str(num))
        diff = 10
        xi = 0
        while diff > 0:
            diff = size - coma_step*xi
            print(diff)
            xi += 1
        print(num,size)
        print(size%coma_step)
        print(xi)


n = 100000
countCommas(n)