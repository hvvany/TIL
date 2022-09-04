n, m, v = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)

answer_bfs=[]
answer_dfs=[]


for _ in range(m):
  i, j = map(int,input().split())
  graph[i].append(j)
  graph[j].append(i)

for i in range(n+1):
  graph[i].sort()

def dfs(n):
  visited[n]=True
  answer_dfs.append(n)
  for num in graph[n]:
    if visited[num] == False:
      dfs(num)

def bfs(n):
  que = list([n])
  visited[n]=True
  while que:
    now = que.pop(0)
    answer_bfs.append(now)
    for i in graph[now]:
      if not visited[i]:
        que.append(i)
        visited[i]=True

dfs(v)
visited=[False]*(n+1)
bfs(v)

print(*answer_dfs)
print(*answer_bfs)