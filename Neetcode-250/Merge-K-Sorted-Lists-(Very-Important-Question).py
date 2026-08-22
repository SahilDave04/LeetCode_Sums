
from utilities import ListNode, only_function, createLinks, printLinks

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> [ListNode]:
        def merge2(l1,l2):
            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return dummy.next

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            showlists = []
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None
                mergedLists.append(merge2(l1,l2))
                #showlists.append(printLinks(merge2(l1,l2),out=1))
            lists = mergedLists
            #print(showlists)
        return lists[0]


lists = [[1,4,5],[1,3,4],[2,6]]        
lists = [createLinks(lst) for lst in lists]
output = only_function("mergeKLists", lists)
printLinks(output)

#Merge K Sorted Lists (Very Important Question)