N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
print(graph)
lst = [0]*(N**2+2)
dx = [0,1,0,-1]
dy = [-1,0,1,0]
def G2L():
  dist = 1
  dir = 0
  idx = 1
  di,dj = (N-1)//2, (N-1)//2
  lst[0] = graph[di][dj]
  while True:
    lst[idx] = graph[di][dj]
    for _ in range(dist):
      print(dist, dir, idx)
      print(di,dj)
      di += dx[dir]
      dj += dy[dir]
      lst[idx] = graph[di][dj]
      idx += 1
      if idx == N**2:
        break
    dir += 1
    dir %= 4
    if dir % 2 == 0:
      dist += 1
G2L()
print(lst)