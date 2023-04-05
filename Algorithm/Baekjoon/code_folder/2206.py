from collections import deque
INF = 10**8
h, w = map(int,input().split())
graph = [list(input()) for _ in range(h)]
inform_graph = [[[INF,INF] for _ in range(w)] for _ in range(h)]
visited = [[[False,False] for _ in range(w)] for _ in range(h)]

dx = [0,-1,1,0]
dy = [1,0,0,-1]
d = deque()
d.append((0,0,0))
inform_graph[0][0][0] = 1
visited[0][0][0] = True
while d:
  i,j,cnt = d.popleft()
  for idx in range(4):
    nx = i + dx[idx]
    ny = j + dy[idx]
    if 0 <= nx < h and 0 <= ny < w:
      if graph[nx][ny] == '0' and visited[nx][ny][cnt] == False:
        visited[nx][ny][cnt] = True
        inform_graph[nx][ny][cnt] = inform_graph[i][j][cnt] + 1
        d.append((nx,ny,cnt))
      elif graph[nx][ny] == '1' and cnt == 0 and visited[nx][ny][1] == False:
        visited[nx][ny][1] = True
        inform_graph[nx][ny][1] = inform_graph[i][j][0] + 1
        d.append((nx,ny,1))

answer = min(inform_graph[h-1][w-1])
if answer == INF:
  print(-1)
else:
  print(answer)