from collections import deque
import sys
input = sys.stdin.readline
h, w = map(int,input().split())
graph = [list(input()) for _ in range(h)]
answer = 0
def solution():
  dx = [0,1,-1,0]
  dy = [1,0,0,-1]
  def bfs(x,y,depth_,visited):
    global answer
    d = deque()
    d.append((x,y,depth_))
    while d:
      (i,j,depth) = d.popleft()
      if depth > answer:
        answer = depth
      for idx in range(4):
        nx = i + dx[idx]
        ny = j + dy[idx]
        if 0 <= nx < h and 0 <= ny < w:
          if graph[nx][ny] == 'L':
            if visited[nx][ny] == False:
              visited[nx][ny] = True
              d.append((nx,ny,depth + 1))
  for i in range(h):
    for j in range(w):
      visited = [[False]*w for _ in range(h)]
      if graph[i][j] == 'L':
        visited[i][j] = True
        bfs(i,j,0,visited)
  return answer
print(solution())