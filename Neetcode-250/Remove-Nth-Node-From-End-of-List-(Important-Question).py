import math
from typing import Optional
from utilities import ListNode, createLinks, printLinks


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:     
        # Adding a Dummy Node as head
        newHead = ListNode(next=head)
        pointer1, pointer2 = newHead, head

        # Setting Pointer2 n places away from Pointer1
        while n > 0 and pointer2:
            pointer2 = pointer2.next
            n -= 1

        # Lopping till the end of the List
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        # Pointer1 is at the spot before the Target element
        pointer1.next = pointer1.next.next

        return newHead.next
        
                
head = [1]
n = 1
worker = Solution()
ans1 = worker.removeNthFromEnd(createLinks(head),n)
print(ans1)

#Remove Nth Node From End of List (Important Question)