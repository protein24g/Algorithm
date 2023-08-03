from collections import deque
def bfs(x, y, find, size, maps):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    q = deque(); q.append([x, y])
    visited = [[-1 for _ in range(size[1])] for _ in range(size[0])]
    visited[x][y] = 0
    while q:
        x, y = q.popleft()
        if maps[x][y] == find: return visited[x][y]
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]
            if 0 <= nx < size[0] and 0 <= ny < size[1]:
                if maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                    q.append([nx, ny]); visited[nx][ny] = visited[x][y] + 1
    return -1
def solution(maps):
    r, c = len(maps), len(maps[0]); answer = 0; s, e, l = 0, 0, 0
    for a, i in enumerate(maps):
        for b, j in enumerate(i):
            if j == 'S': s = [a, b]
            elif j == 'E': e = [a, b]
            elif j == 'L': l = [a, b]
    one = bfs(s[0], s[1], 'L', [r, c], maps)
    if one == -1: return -1
    else:
        two = bfs(l[0], l[1], 'E', [r, c], maps)
        if two == -1: return -1
        else: return one + two