from utilities import classical

class ListNode:
     def __init__(self, val=0, prev=None, next=None):
         self.val = val
         self.next = next
         self.prev = prev         

class MyCircularQueue:

    def __init__(self, k: int):
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, self.left, None)
        self.left.next = self.right
        self.count = 0
        self.k = k

    def traverse(self,head):
        pointer = head
        opt = []
        while pointer != self.right:
            opt.append(pointer.val)
            pointer = pointer.next
        print(opt)

    def isEmpty(self) -> bool:
        #print("ie")
        #self.traverse(self.dummy)
        return self.left.next == self.right

    def isFull(self) -> bool:
        #print("if")
        #self.traverse(self.dummy)
        return self.count == self.k
    
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            new = ListNode(value,self.right.prev,self.right)
            self.right.prev.next = new
            self.right.prev = new
            self.count += 1

        print("e")
        self.traverse(self.left)

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            self.count -= 1
        print("d")
        self.traverse(self.left)
        return True

    def Front(self) -> int:
        print("f")
        self.traverse(self.left)

        if self.isEmpty():
            return -1
        else:
            return self.left.next.val

    def Rear(self) -> int:
        print("r")
        self.traverse(self.left)
        if self.isEmpty():
            return -1
        else:
            return self.right.prev.val



commands = ["MyCircularQueue","enQueue","deQueue","enQueue","enQueue","deQueue","isFull","isFull","Front","deQueue","enQueue","Front","enQueue","enQueue","Rear","Rear","deQueue","enQueue","enQueue","Rear","Rear","Front","Rear","Rear","deQueue","enQueue","Rear","deQueue","Rear","Rear","Front","Front","enQueue","enQueue","Front","enQueue","enQueue","enQueue","Front","isEmpty","enQueue","Rear","enQueue","Front","enQueue","enQueue","Front","enQueue","deQueue","deQueue","enQueue","deQueue","Front","enQueue","Rear","isEmpty","Front","enQueue","Front","deQueue","enQueue","enQueue","deQueue","deQueue","Front","Front","deQueue","isEmpty","enQueue","Rear","Front","enQueue","isEmpty","Front","Front","enQueue","enQueue","enQueue","Rear","Front","Front","enQueue","isEmpty","deQueue","enQueue","enQueue","Rear","deQueue","Rear","Front","enQueue","deQueue","Rear","Front","Rear","deQueue","Rear","Rear","enQueue","enQueue","Rear","enQueue"]
inputs = [[81],[69],[],[92],[12],[],[],[],[],[],[28],[],[13],[45],[],[],[],[24],[27],[],[],[],[],[],[],[88],[],[],[],[],[],[],[53],[39],[],[28],[66],[17],[],[],[47],[],[87],[],[92],[94],[],[59],[],[],[99],[],[],[84],[],[],[],[52],[],[],[86],[30],[],[],[],[],[],[],[45],[],[],[83],[],[],[],[22],[77],[23],[],[],[],[14],[],[],[90],[57],[],[],[],[],[34],[],[],[],[],[],[],[],[49],[59],[],[71]]
classical(commands,inputs,"MyCircularQueue")


#Design Circular Queue (Important Question)