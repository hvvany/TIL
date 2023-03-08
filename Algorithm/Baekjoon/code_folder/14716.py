import sys
sys.setrecursionlimit(10**6)

m, n = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]

def dfs(i,j):
    dx = [-1,-1,-1,0,1,1,1,0]
    dy = [-1,0,1,1,1,0,-1,-1]
    if graph[i][j] == 1:
        graph[i][j] = 0
        for idx in range(8):
            _x = i + dx[idx]
            _y = j + dy[idx]
            if 0 <= _x < m and 0 <= _y < n:
                if graph[_x][_y] == 1:
                    dfs(_x,_y)
answer = 0
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            answer += 1
            dfs(i,j)
print(answer)