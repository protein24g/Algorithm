from collections import deque
d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def solution(maps):
    def bfs(maps):
        n, m = len(maps[0]), len(maps)
        visited = [[-1 for _ in range(n)] for _ in range(m)]
        q = deque(); q.append([0, 0]); visited[0][0] = 1
        while q:
            x, y = q.popleft()
            if x == m-1 and y == n-1: return visited[m-1][n-1]
            for i in range(4):
                nx, ny = x + d[i][0], y + d[i][1]
                if 0 <= nx < m and 0 <= ny < n:
                    if visited[nx][ny] == -1 and maps[nx][ny] == 1:
                        q.append([nx, ny])
                        visited[nx][ny] = visited[x][y] + 1
        return -1
    return bfs(maps)