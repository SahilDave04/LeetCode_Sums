from collections import deque


class MyStack:
    def __init__(self):
        self.queue = deque()

    def empty(self) -> bool:
        if self.queue == deque():
            return True
        else:
            return False

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if not self.empty():
            for _ in range(len(self.queue)-1):
                self.push(self.queue.popleft())
            return self.queue.popleft()

    def top(self) -> int:
        if not self.empty():
            return self.queue[-1]

    


s = "{}"
worker = MyStack()
commands = [worker.empty()]
for c in commands:
    print(c)

#Implement Stack using Queues