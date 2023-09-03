d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(x, y, visited, grid):
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + d[i][0], y + d[i][1]
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == '1' and visited[nx][ny] == 0:
                dfs(nx, ny, visited, grid)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    dfs(i, j, visited, grid)
                    cnt += 1
        return cnt
