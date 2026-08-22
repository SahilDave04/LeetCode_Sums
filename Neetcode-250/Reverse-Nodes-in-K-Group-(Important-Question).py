from utilities import ListNode, only_function, createLinks, printLinks

class Solution:
    def reverseKGroup(self, head: [ListNode], k: int) -> [ListNode]:
        def get_Kth(curr,k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        
        dummy = ListNode(0,head)
        groupPrev = dummy
        
        while True:
            kth = get_Kth(groupPrev,k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            nxt = groupPrev.next
            groupPrev.next = kth
            groupPrev = nxt

        return dummy.next


head = [1,2,3,4,5]
k = 2
output = only_function("reverseKGroup", createLinks(head), k)
printLinks(output)

#Reverse Nodes in K-Group (Important Question)