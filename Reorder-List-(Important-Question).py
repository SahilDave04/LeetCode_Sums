import math
from typing import Optional
from utilities import ListNode, createLinks, printLinks


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        # Getting to the Middle using the Fast and Slow Pointer technique
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reversing the Second Half 
        curr,prev = slow.next, None
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        sHead = prev

        # Merging both the Halves 
        p1,p2 = head,sHead
        while p1 and p2:
            n1,n2 = p1.next, p2.next
            p1.next, p2.next = p2, n1
            p1, p2 = n1, n2

        
                
head = [1,2,3,4]
worker = Solution()
ans1 = worker.reorderList(createLinks(head))
print(ans1)

#Reorder List (Important Question)