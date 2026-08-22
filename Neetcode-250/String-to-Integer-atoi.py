def myAtoi(s):
    final_num = 0
    low_limit = -2**31
    up_limit = (2**31)-1
    striped = s.strip()
    print(striped)
    stack = []
    for l in range(len(striped)):
        print(striped[l])
        print(type(striped[l]))
        if l == 0:
            if striped[l] == "-" or striped[l] == "+" or striped[l] == "0" or striped[l].isdigit() == True:
                stack.append(striped[l])
        else:
            print("here")
            print(str(".").isdigit())
            print(striped[l].isdigit())
            if striped[l].isdigit() == True:
                print("there")
                if striped[l] != '0':
                    stack.append(striped[l])
                else:
                    pass
            else:
                print("nooo")
                break
    print(stack)
    if stack != []:
        final_num = int(str("".join(stack)))
        if final_num > up_limit:
            final_num = up_limit
        elif final_num < low_limit:
            final_num = low_limit
    print(final_num)
    print(type(final_num))
    return final_num
    

string = ".1"
myAtoi(string)
#this is not the right solution