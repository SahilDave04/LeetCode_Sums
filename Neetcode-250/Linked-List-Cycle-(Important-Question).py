import math
from typing import Optional
from utilities import ListNode, createLinks


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        Spointer, Fpointer = head, head
        # slow_pointer [moves by 1], fast_pointer [moves by 2]

        while Fpointer and Fpointer.next:
            Spointer = Spointer.next
            Fpointer = Fpointer.next.next

            if Spointer == Fpointer:
                return True

        return False

        
head = [3,2,0,-4]
pos = 1
worker = Solution()
ans1 = worker.hasCycle(createLinks(head,createCircle=1,connect=pos))
print(ans1)

#Linked List Cycle (Important Question)