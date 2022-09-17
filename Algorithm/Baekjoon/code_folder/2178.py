from collections import deque

from pprint import pprint

n, m = map(int,input().split())
graph = [list(map(int,list(input()))) for _ in range(n)]
queue = deque()
long = []
# pprint(graph)

graph[0][0] = 1
queue.append((0,0))
while queue:
  (x,y) = queue.popleft()
  dx = [-1, 0, 0, 1]
  dy = [0, 1, -1, 0]

  for k in range(4):
    _x = x + dx[k]
    _y = y + dy[k]

    if 0 <= _x < n and 0 <= _y < m:
      if graph[_x][_y] == 1:
        queue.append((_x,_y))
        graph[_x][_y] = graph[x][y] + 1
# pprint(graph)
print(graph[n-1][m-1])