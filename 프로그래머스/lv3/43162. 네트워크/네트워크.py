def solution(n, computers):
    def dfs(v):
        visited[v] = 1
        for i in range(n):
            if visited[i] == 0 and computers[v][i]:
                dfs(i)
        
    count = 0   
    visited = [0 for _ in range(n)]
    for idx in range(n):
        if visited[idx] == 0:
            dfs(idx)
            count += 1
    return count