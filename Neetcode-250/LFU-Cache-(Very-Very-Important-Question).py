from utilities import classical, printLinks

from collections import defaultdict

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None


class DLL:

    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.size = 0

    def add(self,node):
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

        self.size += 1

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

    def remove_last(self):
        if self.size > 0:
            node = self.tail.prev
            self.remove(node)
            return node
        return None


class LFUCache:

    def __init__(self,capacity:int):
        self.capacity = capacity
        self.keyMap = {}
        self.freqMap = defaultdict(DLL)
        self.minFreq = 0

    def get(self,key:int)->int:
        print("g ", key)
        
        if key not in self.keyMap:
            return -1

        node = self.keyMap[key]
        self.update(node)

        print(self.freqMap)
        print(self.keyMap)

        return node.value

    def put(self,key:int,value:int)->None:
        print("p ", key)

        if self.capacity == 0:
            return

        if key in self.keyMap:
            node = self.keyMap[key]
            node.value = value
            self.update(node)

            print(self.freqMap)
            print(self.keyMap)

            return

        if len(self.keyMap) == self.capacity:
            list = self.freqMap[self.minFreq]
            removed = list.remove_last()
            del self.keyMap[removed.key]

        node = Node(key,value)
        self.keyMap[key] = node

        self.minFreq = 1
        self.freqMap[1].add(node)

        print(self.freqMap)
        print(self.keyMap)

    def update(self,node):
        
        freq = node.freq
        list = self.freqMap[freq]

        list.remove(node)

        if freq == self.minFreq and list.size == 0:
            self.minFreq += 1

        node.freq += 1

        self.freqMap[node.freq].add(node)
        
        
                
commands = ["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
inputs = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]
classical(commands,inputs,commands[0])


#LFU Cache (Very Very Important Question)