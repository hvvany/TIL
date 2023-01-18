t = int(input())

def search(r,c):
    for idx in range(4):
      _r = r + dr[idx]
      _c = c + dc[idx]
      if 0 <= _r < h and 0 <= _c < w and graph[_r][_c] == '#':
        graph[_r][_c] = '.'
        search(_r,_c)

for _ in range(t):
  h, w = map(int,input().split())
  graph = [list(input()) for _ in range(h)]
  answer = 0
  dr = [-1,0,1,0]
  dc = [0,1,0,-1]
  for r in range(h):
    for c in range(w):
      if graph[r][c] == '#':
        answer += 1
        graph[r][c] = '.'
        search(r,c)
  print(answer)