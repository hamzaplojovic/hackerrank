def fairRations(B):
    count = 0
    for i in range(len(B)-1):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i+1] += 1
            count += 2
    if B[-1] % 2 != 0:
        return "NO"
    else:
        return str(count)