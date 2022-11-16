def sockMerchant(n, ar):
    ar.sort()
    count = 0
    for x in range(len(ar)):
        if x == len(ar)-1:
            break
        if ar[x] == ar[x+1]:
            count += 1
            ar[x] = 0
            ar[x+1] = 0
    return count