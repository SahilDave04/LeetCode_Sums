from collections import deque


class MyQueue:
    def __init__(self):
        self.s1 = list()
        self.s2 = list()

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self) -> bool:
        return max(len(self.s1),len(self.s2)) == 0
    

s = "{}"
worker = MyQueue()
commands = [worker.push(4),worker.push(9),worker.peek(),worker.pop(),worker.peek(),worker.empty()]
for c in commands:
    print(c)

#Implement Queue using Stacks