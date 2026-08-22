from utilities import classical

class ListNode:
    def __init__(self, key, val):
         self.key, self.val = key, val
         self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity

        # Creating a Doubly Linked List with Start and End dummy nodes
        self.left = ListNode(0,0)
        self.right = ListNode(0,0)
        self.left.next, self.right.prev = self.right, self.left

        # Structure: {key:ListNode(key,value)}
        self.cache = dict()  

    def remove(self,node):
        prv,nxt = node.prev,node.next
        prv.next,nxt.prev = nxt,prv

    def insert(self,node):
        prv,nxt = self.right.prev,self.right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = ListNode(key,value)
        self.insert(self.cache[key])

        # Handling the LRU after insertion 
        if len(self.cache) > self.capacity:
            self.cache.pop(self.left.next.key)
            self.remove(self.left.next)

                        
commands = ["LRUCache","put","put","get","put","get","put","get","get","get"]
inputs = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
classical(commands,inputs,commands[0])


#LRU Cache (Very Important Question)