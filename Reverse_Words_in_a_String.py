s = "a good   example"
p = s.strip()
b1 = p.split(" ")
print(b1)
while "" in b1:
        b1.remove("")
b2 = b1[::-1]
print(b2)
wrd = ""
for i in b2:
        wrd = wrd + " " + i
fn_wrd = wrd.strip()

print(fn_wrd)
