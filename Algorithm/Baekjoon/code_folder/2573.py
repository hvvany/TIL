from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
# visited = [[False] * m for _ in range(n)]
# memory = set()

# 전체 돌면서 섬의 개수 구하기(재귀)
# 방문 처리로 뺄 값 저장 후 한번에 빼야함...실시간 빼면 오류
dx = [-1,0,0,1]
dy = [0,1,-1,0]
depth = 0

temp = deque()
def BingCnt(i,j):
  temp.append((i,j))
  while temp:
    i, j = temp.popleft()
    for idx in range(4):
      _x = i + dx[idx]
      _y = j + dy[idx]
      if(0 < _x < n-1 and 0 < _y < m-1):
        if graph[_x][_y] != 0:
          if visited[_x][_y] == False:
            visited[_x][_y] = True
            temp.append((_x, _y))
  else:
    return

def BingMelt(i,j):
  if(graph[i][j] != 0):
    cnt = 0
    for idx in range(4):
      _x = i + dx[idx]
      _y = j + dy[idx]
      if(0 <= _x < n and 0 <= _y < m):
        if(graph[_x][_y] == 0):
          cnt += 1
    memory.append((i,j,cnt))

answer = 0
year = 0
breaker = False
for _ in range(1500):
  visited = [[False] * m for _ in range(n)]
  # 빙산 개수 카운트 => 2이면 종료 할 것
  cnt = 0
  for i in range(1,n-1):
    for j in range(1,m-1):
      if(graph[i][j] != 0):
        if visited[i][j] == False:
          visited[i][j] = True
          BingCnt(i,j)
          cnt += 1
          if cnt >= 2:
            answer = year
            breaker = True
            break
    if breaker:
      break
  if breaker:
    break
  # 빙산 한 주기 녹임 => 실시간으로 빼면 안됨 => 저장
  memory = []
  for i in range(1,n-1):
    for j in range(1,m-1):
      BingMelt(i,j)

  for inform in memory:
    i,j,cnt = inform
    graph[i][j] -= cnt
    if graph[i][j] < 0:
      graph[i][j] = 0
  year += 1
print(answer)




# import sys
# from collections import deque
# sys.setrecursionlimit = 10**6

# n, m = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]
# # visited = [[False] * m for _ in range(n)]
# memory = [[0]*m for _ in range(n)]

# # 전체 돌면서 섬의 개수 구하기(재귀)
# # 방문 처리로 뺄 값 저장 후 한번에 빼야함...실시간 빼면 오류
# dx = [-1,0,0,1]
# dy = [0,1,-1,0]
# depth = 0
# temp = deque()
# def BingCnt(i,j):
#   temp.append((i,j))
#   while(temp):
#     (i,j) = temp.popleft()
#     for idx in range(4):
#       _x = i + dx[idx]
#       _y = j + dy[idx]
#       if(0 < _x < n-1 and 0 < _y < m-1):
#         if graph[_x][_y] != 0:
#           if visited[_x][_y] == False:
#             visited[_x][_y] = True
#             print(f'x_ : {_x}, y_ : {_y}')
#             temp.append((_x,_y))
#   return

# def BingMelt(i,j):
#   if(graph[i][j] != 0):
#     cnt = 0
#     for idx in range(4):
#       _x = i + dx[idx]
#       _y = j + dy[idx]
#       if(graph[_x][_y] == 0):
#         cnt += 1
#     memory[i][j] = cnt

# answer = 0
# year = 0
# while True:
#   visited = [[False] * m for _ in range(n)]
#   # 빙산 개수 카운트 => 2이면 종료 할 것
#   cnt = 0
#   for i in range(1,n-1):
#     for j in range(1,m-1):
#       if(graph[i][j] != 0):
#         if visited[i][j] == False:
#           visited[i][j] = True
#           BingCnt(i,j)
#           cnt += 1
#   if cnt >= 2:
#     answer = year
#     break
#   # 빙산 한 주기 녹임 => 실시간으로 빼면 안됨 => 저장
#   memory = [[0]*m for _ in range(n)]
#   for i in range(1,n-1):
#     for j in range(1,m-1):
#       BingMelt(i,j)
#       cnt += 1

#   for i in range(1,n-1):
#     for j in range(1,m-1):
#       if(memory[i][j] != 0):
#         graph[i][j] -= memory[i][j]
#         if graph[i][j] < 0:
#           graph[i][j] = 0
#   year += 1
# print(answer)