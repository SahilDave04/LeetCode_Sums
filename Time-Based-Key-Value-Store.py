class TimeMap:
    def __init__(self):
        self.timings = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timings[key] = self.timings.get(key,[])
        self.timings[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.timings.get(key,[])
        l,r = 0,len(values)-1
        res = ""
        while l <= r:
            m = (l+r)//2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        
 
commands = ["TimeMap","set","set","get","get","get","get","get"]
arguments = [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

output = []
obj = None

for cmd, args in zip(commands, arguments):
    if cmd == "TimeMap":
        # Instantiate the class
        obj = TimeMap(*args)
        output.append(None)
    else:
        # Dynamically find and call the method
        method = getattr(obj, cmd)
        result = method(*args)
        output.append(result)
print(output)

#Time Based Key-Value Store