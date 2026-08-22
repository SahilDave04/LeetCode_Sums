class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head):
        def recursive(head):
            if not head:
                return None

            newHead = head
            while head.next:
                print(head)
                newHead = recursive(head.next)
                head.next.next = head
            head.next = None

            return newHead

        def iterative(head):
            prev,curr = None, head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        return recursive(head),iterative(head)
        
head = [1,2,3,4,5]
worker = Solution()
ans1 = worker.reverseList(head)
print(ans1)

#Reverse Linked List (Important Question)