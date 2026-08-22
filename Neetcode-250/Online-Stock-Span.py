class StockSpanner:
    def __init__(self):
        self.stack = list() # [price, span]

    def next(self, price: int) -> int:   
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price,span])
        return span
            

worker = StockSpanner()
commands = [worker.next(100),worker.next(80),worker.next(60),worker.next(70),worker.next(60),worker.next(75),worker.next(85)]
for c in commands:
    print(c)

#Online Stock Span