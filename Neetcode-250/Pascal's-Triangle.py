def generate(numRows):
    rows = []
    if numRows == 1:
        rows.append([1])
    else:
        temp = []
        rows = generate(numRows-1)
        inFocus = rows[numRows-2]
        for i in range(len(inFocus)+1):
            if i < len(inFocus) and i-1 > -1:
                temp.append(inFocus[i-1]+inFocus[i])
            elif i-1 < 0:
                temp.append(inFocus[i])
            elif i == len(inFocus):
                temp.append(inFocus[i-1])
        rows.append(temp)
    return rows

numRows = 5
pascalsTriangle = generate(numRows)
print(pascalsTriangle)

