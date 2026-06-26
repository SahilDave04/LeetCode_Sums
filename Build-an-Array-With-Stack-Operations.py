'''Problem Link - LINK'''
 
def buildArray(target,n):
    stack = []
    actions = []
    num = 1
    while stack != target and num < n:
        if stack == []:
            stack.append(num)
            num += 1
            actions.append("PUSH")
        elif stack != target[len(stack)-1]:
            stack.pop()
            actions.append("POP")
        else:
            stack.append(num)
            actions.append("PUSH")
        print(stack,target[len(stack)-1])
        print(actions)
    return actions
            
target = [1,3]
n = 3
buildArray(target,n)