def findDigits(n):
    count = 0
    for x in str(n):
        if int(x) != 0 and n % int(x) == 0:
            count += 1
    return count
