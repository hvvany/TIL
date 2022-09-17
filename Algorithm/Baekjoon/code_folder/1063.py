# 반복문 실행하며 돌의 주변 탐색도 하여 방문 기록 반대 방향으로 이동
# 킹이나 돌이 범우 밖이면 통과

k, r, n = input().split()
r = list(r)
r = (ord(r[0])-65,int(r[1])-1)
k = list(k)
k = (ord(k[0])-65,int(k[1])-1)

graph = [[0]*8 for _ in range(8)]

for i in range(int(n)):
  move = input()
  if 'R' in move:
    _x = 1
  elif 'L' in move:
    _x = -1
  else:
    _x = 0
  if 'T' in move:
    _y = 1
  elif 'B' in move:
    _y = -1
  else:
    _y = 0
  ( x, y ) = k
  nx = x + _x
  ny = y + _y
  if 0 <= nx < 8 and 0 <= ny < 8:
    if r == (nx,ny):
      ( i, j ) = r
      ni = i + _x
      nj = j + _y
      if 0 <= ni < 8 and 0 <= nj < 8:
        r = (ni,nj)
        k = (nx,ny)
    else:
      k = (nx,ny)
print(f'{chr(k[0]+65)}{k[1]+1}')
print(f'{chr(r[0]+65)}{r[1]+1}')