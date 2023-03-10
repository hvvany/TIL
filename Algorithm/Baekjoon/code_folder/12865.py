n, k = map(int,input().split())
graph = [list([0]*(k+1)) for _ in range(n+1)]
for i in range(1,n+1):
  w, v = map(int,input().split())
  for j in range(1,k+1):
    if j < w:
      graph[i][j] = graph[i-1][j]
    elif j >= w:
      graph[i][j] = max(graph[i-1][j-w] + v, graph[i-1][j])
print(graph[n][k])