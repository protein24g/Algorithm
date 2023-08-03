from collections import deque
def bfs(x, ary, visited):
    cnt = 0
    q = deque([x])
    visited[x] = 1
    
    while q:
        x = q.popleft()
        cnt += 1
        for i in ary[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
    return cnt

def solution(n, wires):
    answer = 0
    #print(n, wires)
    min_res = 1e9
    for i in range(len(wires)):
        ary = [[] for _ in range(n+1)]
        visited = [0 for _ in range(n+1)]
        for j in range(len(wires)):
            if i != j:
                a, b = wires[j]
                ary[a].append(b); ary[b].append(a)
                #print(wires[j], end=' ')
        #print('\n', ary[1:])
        #print()
        
        for i, j in enumerate(visited[1:]):
            if visited[i+1] == 0:
                #visited[i+1] = 1
                tmp = bfs(i+1, ary, visited)
                min_res = min(min_res, abs(tmp - abs(n - tmp)))
                pass
            #print(i+1, '->', j)
        #print('min_res = ', min_res)
        
    
    return min_res