class FreqStack:

    def __init__(self):
        self.stacks = dict()   # This holds the numbers for each frequency
        self.counts = dict()   # This holds the frequency of each unique number
        self.high = 0          # This represents the max frequency till now


    def push(self, val: int) -> None:
        cVal = 1 + self.counts.get(val,0)
        self.counts[val] = cVal
        if cVal > self.high:
            self.high = cVal
            self.stacks[cVal] = []
        self.stacks[cVal].append(val)
        print(self.stacks,self.counts,self.high)


    def pop(self) -> int:
        res = self.stacks[self.high].pop()
        self.counts[res] -= 1
        if not self.stacks[self.high]:
            self.high -= 1
        print(self.stacks,self.counts,self.high)
        return res



freqStack = FreqStack()
commands = [freqStack.push(5),freqStack.push(7),freqStack.push(5),freqStack.push(7),freqStack.push(4),freqStack.push(5),freqStack.pop(),freqStack.pop(),freqStack.pop(),freqStack.pop()]
for c in commands:
    print(c)

#Maximum Frequency Stack (Important Question)