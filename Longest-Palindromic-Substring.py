def longestPalindrome(s):
    win = len(s)
    longPal = None
    while win > 0:
        shorts = [s[i:i+win] for i in range(len(s)) if i <= len(s)-win]
        print(shorts)
        for short in shorts:
            if short[::-1] == short:
                print("here")
                longPal = short
                print(longPal)                
                return longPal
        win -= 1

string = 'babad'
longestPalindrome(string)