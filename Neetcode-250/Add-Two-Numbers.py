from typing import Optional
from utilities import ListNode, createLinks, printLinks

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:    
        carry = 0
        sums = ListNode()
        p1,p2, new = l1,l2, sums
 
        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            sm = v1+v2+carry
            carry = sm//10
            new.next = ListNode(sm%10)
            new = new.next
            p1 = p1.next if p1 else p1
            p2 = p2.next if p2 else p2

        if carry != 0: new.next = ListNode(carry)

        return sums.next

        
                
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
worker = Solution()
ans1 = worker.addTwoNumbers(createLinks(l1),createLinks(l2))
print(ans1)

#Add Two Numbers