from typing import Optional
from utilities import ListNode, createLinks, printLinks

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        l1,cur = dummy,head

        # This Loop runs till we reach Left, l1-> node before Left, cur-> Left
        for i in range(left-1):
            l1,cur = cur, cur.next

        # This Loops run till we reach Right, prev-> Right, cur-> node after Right
        prev = None
        for i in range(right-left+1):
            temp = cur.next
            cur.next = prev
            prev, cur = cur, temp

        # Setting Pointers, l1->right, left->cur
        l1.next.next = cur
        l1.next = prev
        
        return dummy.next
        
                
head = [5]
left = 1
right = 1
worker = Solution()
ans1 = worker.reverseBetween(createLinks(head),left,right)
print(ans1)

#Reverse Linked List II (Important Question)