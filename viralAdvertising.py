def viralAdvertising(n):
    shared = 5
    liked = 0
    cumulative = 0
    for x in range(n):
        liked = shared // 2
        shared = liked * 3
        cumulative += liked
    return cumulative   