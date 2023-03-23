from collections import deque

def bfs():
  d = deque()
  d.append(start_point)
  while d:
    x, y = d.popleft()
    if abs(x - end_point[0]) + abs(y - end_point[1]) <= 1000:
      print('happy')
      return
    for i in range(n):
      nx, ny = store_lst[i][0], store_lst[i][1]
      if visited[i] == False and abs(nx - x) + abs(ny - y) <= 1000:
        visited[i] = True
        d.append((nx,ny))
  print('sad')
  
T = int(input())
for _ in range(T):
  n = int(input())
  start_point = tuple(map(int,input().split()))
  store_lst = []
  for i in range(n):
    store_lst.append(tuple(map(int,input().split())))
  end_point = tuple(map(int,input().split()))
  visited = [False]*n
  bfs()