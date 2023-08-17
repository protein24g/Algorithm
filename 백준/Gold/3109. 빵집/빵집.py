import sys
input = sys.stdin.readline

R, C = list(map(int, input().strip().split()))
map_data = []
for _ in range(R):
    map_data.append(list(input().strip()))
    
visited = [[0 for _ in range(C)] for _ in range(R)]
moves = [(-1, 1), (0, 1), (1, 1)]

def dfs(cpos):
    cy, cx = cpos
    if cx == C - 1:
        return 1

    for move in moves:
        ny, nx = cy + move[0], cx + move[1]
        if 0 <= ny < R and 0 <= nx < C:
            if visited[ny][nx] == 0 and map_data[ny][nx] == '.':
                visited[ny][nx] = 1
                dfs_ret = dfs((ny, nx))
                if dfs_ret == 1:
                    return dfs_ret

    return 0

result = 0
for y in range(R):
    result += dfs((y, 0))
print(result)
