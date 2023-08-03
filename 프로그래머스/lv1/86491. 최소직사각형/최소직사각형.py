def solution(sizes):
    x, y = 0, 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            tmp = sizes[i][0]
            sizes[i][0] = sizes[i][1]
            sizes[i][1] = tmp
        if sizes[i][0] > x:
            x = sizes[i][0]
        if sizes[i][1] > y:
            y = sizes[i][1]
    return x*y