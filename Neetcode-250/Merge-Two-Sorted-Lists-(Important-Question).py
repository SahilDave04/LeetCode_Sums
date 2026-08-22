import math
from typing import Optional
from utilities import ListNode, createLinks


class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyStart = ListNode() # This is a empty Listnode for giving a start
        pointer = dummyStart

        while l1 and l2:
            if l1.val < l2.val:
                pointer.next = l1
                l1 = l1.next
            else:
                pointer.next = l2
                l2 = l2.next
            pointer = pointer.next
        
        if l1:
            pointer.next = l1
        if l2:
            pointer.next = l2

        return dummyStart.next  # We are skipping the dummyStart node which was empty

        
list1 = [1,2,4]
list2 = [1,3,4]
worker = Solution()
ans1 = worker.mergeTwoLists(createLinks(list1),createLinks(list2))
print(ans1)


#Merge Two Sorted Lists (Important Question)