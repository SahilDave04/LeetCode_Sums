def fib(n):
    if n <= 1:
        if n == 0:
            return 0
        elif n == 1:
            return 1
    else:
        addy = fib(n-1) + fib(n-2)
        return addy

n = 4
fn = fib(n)
print(fn)