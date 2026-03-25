def firstUniqueEven(nums):
    evens = [i for i in nums if i%2 == 0]
    print(evens)
    the_one = False
    for j in evens:
        if evens.count(j) == 1:
            the_one = True
            return j
        else:
            pass
    if the_one == False:
        return -1

nums = [3,4,2,5,4,6]
inti = firstUniqueEven(nums)
print(inti)