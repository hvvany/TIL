t = int(input())
for _ in range(t):
  w, h, k = map(int,input().split())
  ground = [[0]*w for _ in range(h)]
  for _ in range(k):
    x,y = map(int,input().split())
    ground[y][x] = 1

  def dfs(x, y) :
    dx = [-1, 0, 0, 1]
    dy = [ 0, 1, -1, 0]
    for i in range(4) :
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < w and 0 <= ny < h :
        if ground[ny][nx] == 1 :
          ground[ny][nx] = 0
          dfs(nx, ny)
  worm = 0
  for i in range(w) :
    for j in range(h) :
      if ground[j][i] == 1 :
        dfs(i, j)
        worm += 1
  print(worm)