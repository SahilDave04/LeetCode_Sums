from typing import Optional
from utilities import ListNode, createLinks, printLinks

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        nodes = {None:None}
        pointer = head
        while pointer:
            copy = Node(pointer.val)
            nodes[pointer] = copy
            pointer = pointer.next
        
        pointer = head
        while pointer:
            copy = nodes[pointer]
            print(copy.val,pointer.next,pointer.random)
            copy.next = nodes[pointer.next]
            copy.random = nodes[pointer.random]
            pointer = pointer.next
        
        return nodes[head]
        
                
head = [[7,None],[13,0],[11,4],[10,2],[1,0]]
worker = Solution()
ans1 = worker.copyRandomList(createLinks2(head))
print(ans1)

#Copy List with Random Pointer