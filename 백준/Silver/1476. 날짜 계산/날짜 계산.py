E, S, M = list(map(int, input().split()))

tmpA, tmpB, tmpC, count = 1, 1, 1, 1
while 1:
    if tmpA == E and tmpB == S and tmpC == M:
        print(count)
        break
    else:
        count += 1
        tmpA += 1
        if tmpA > 15:
            tmpA = 1
        tmpB += 1
        if tmpB > 28:
            tmpB = 1
        tmpC += 1
        if tmpC > 19:
            tmpC = 1
        