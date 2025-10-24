def reverser(s):
    size = len(s)
    reverses = {']':'[',")":"(","}":"{"}
    k = 0
    v = 0
    stack = []
    if size%2 == 0:
        for b in s:
            if b in reverses.values():
                stack.append(b)
                v += 1
            elif b in reverses.keys():
                if stack != []:
                    if stack[len(stack)-1] == reverses[b]:
                        stack.pop()
                    else:
                        return False
                else:
                    pass
                k += 1
        if k == v and stack == []:
            return True
        else:
            return False
    else:
        return False

string = '))(('
verdict = reverser(str(string))
print(verdict)