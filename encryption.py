import math

def encryption(s):
    s = s.replace(" ", "")
    l = len(s)
    rows = math.floor(math.sqrt(l))
    cols = math.ceil(math.sqrt(l))
    if rows * cols < l:
        rows += 1
    result = ""
    for i in range(cols):
        for j in range(rows):
            if i + j * cols < l:
                result += s[i + j * cols]
        result += " "
    return result