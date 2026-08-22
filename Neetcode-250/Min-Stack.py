class MinStack:

    def __init__(self):
        self.minStk = list()
        self.stk = list()

    def push(self, value: int) -> None:
        self.stk.append(value)
        value = min(value,self.minStk[-1] if self.minStk else value)
        self.minStk.append(value)
        print(self.minStk,self.stk)

    def pop(self) -> None:
        self.stk.pop()
        self.minStk.pop()
        print(self.minStk,self.stk)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minStk[-1]


worker = MinStack()
commands = [worker.push(4),worker.push(9),worker.push(2),worker.pop(),worker.getMin()]
for c in commands:
    print(c)


#Min Stack