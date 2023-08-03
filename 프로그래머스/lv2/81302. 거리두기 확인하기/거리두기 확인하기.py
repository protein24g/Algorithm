from collections import deque
def solution(places):
    def bfs(x, y, ary):
        visited = [[0 for _ in range(5)] for _ in range(5)]
        q = deque()
        q.append([x, y])
        visited[x][y] = 1

        while q:
            x, y = q.popleft()
            if ary[x][y] == 'P' and visited[x][y] <= 3 and visited[x][y] != 1:
                return 0
            for i in range(4):
                nx, ny = x + d[i][0], y + d[i][1]
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if visited[nx][ny] == 0:
                        if ary[nx][ny] != 'X':
                            visited[nx][ny] = visited[x][y] + 1
                            q.append([nx, ny])
        return 1
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]       
    answer = []
    for ary in places:
        chk = 1
        for i in range(5):
            for j in range(5):
                if ary[i][j] == 'P':
                    chk = min(chk, bfs(i, j, ary))
        answer.append(chk)
                        
        
    return answer
