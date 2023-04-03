import sys
input = sys.stdin.readline

graph = [list(map(int,input().rstrip())) for _ in range(9)]
col_set = [set() for _ in range(9)]
row_set = [set() for _ in range(9)]
group_set = [set() for _ in range(9)]

def rowCheck(i,j,target):
  for idx in range(9):
    if target == graph[i][idx]:
      return False
  return True

def colCheck(i,j,target):
  for idx in range(9):
    if target == graph[idx][j]:
      return False
  return True

def groupCheck(i,j,target):
  group_center = (0,0)
  if j < 3:
    if i < 3:
      group_center = (1,1)
    elif i < 6:
      group_center = (4,1)
    else:
      group_center = (7,1)
  elif j < 6:
    if i < 3:
      group_center = (1,4)
    elif i < 6:
      group_center = (4,4)
    else:
      group_center = (7,4)
  else:
    if i < 3:
      group_center = (1,7)
    elif i < 6:
      group_center = (4,7)
    else:
      group_center = (7,7)
  dx = [0,-1,-1,-1,0,0,1,1,1]
  dy = [0,-1,0,1,-1,1,-1,0,1]
  x, y = group_center
  for idx in range(9):
    nx = x + dx[idx]
    ny = y + dy[idx]
    if 0 <= nx < 9 and 0 <= ny < 9:
      if target == graph[nx][ny]:
        return False
  return True

def checkAuto(i,j,target):
  return rowCheck(i,j,target) & colCheck(i,j,target) & groupCheck(i,j,target)

def bt(cnt):
  if cnt == len(zero_lst):
    for i in range(9):
      for j in range(9):
        print(graph[i][j],end='')
      print()
    return
  x, y = zero_lst[cnt]
  for num in range(1,10):
    if checkAuto(x,y,num):
      graph[x][y] = num
      bt(cnt + 1)
      graph[x][y] = 0

zero_lst = []
for i in range(9):
  for j in range(9):
    if graph[i][j] == 0:
      zero_lst.append((i,j))
print('----------------------')
bt(0)