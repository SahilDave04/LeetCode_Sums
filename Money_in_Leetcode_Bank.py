def totalMoney(n):
    latest_mon = 0
    total = 0
    prev = 0
    for d in range(n):
        if d == 0 or d%7 == 0:
            latest_mon += 1
            prev = latest_mon
            total += latest_mon
        else:
            total += prev+1
            prev += 1
    return total

n = 20 #this is number of days
totalMoney(20)