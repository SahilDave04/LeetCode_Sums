'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
'''

def first_occurence(haystack,needle):
    sizeof_haystck = len(haystack)
    sizeof_needle = len(needle)
    if sizeof_needle < sizeof_haystck:
        max_point = sizeof_haystck - sizeof_needle + 1
        print(haystack[0:max_point])
        for i in range(max_point):
            window = haystack[i:i+sizeof_needle]
            print(window)
            print(needle)
            if window == needle:
                return i
        return -1
    else:
        if sizeof_needle == sizeof_haystck:
            if needle == haystack:
                return 0
        elif sizeof_needle > sizeof_haystck:
            return -1
