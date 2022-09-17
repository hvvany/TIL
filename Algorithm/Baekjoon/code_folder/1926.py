# import sys
# sys.setrecursionlimit(10**6)     # 재귀 함수 깊이 제한 풀기

# h, w = map(int,input().split())
# graph = [[0]*w for _ in range(h)]
# area = []
# pic_cnt = 0
# for i in range(h):
#   graph[i] = list(map(int,input().split()))

# def Picture(x,y):
#   global cnt
#   dx = [-1, 0, 0, 1]     # 4방 탐색
#   dy = [0, 1, -1, 0]
#   if graph[y][x] == 1:   # 1이면 4방 탐색 시작
#     cnt += 1
#     graph[y][x] = 0      # 방문시 0으로 변환
#     for i in range(4):
#       _x = x + dx[i]
#       _y = y + dy[i]
#       if 0 <= _x < w and 0 <= _y < h:  # 범위 조건
#         if graph[_y][_x] == 1:
#           Picture(_x,_y)

# for i in range(w):
#   for j in range(h):
#     if graph[j][i] == 1:
#       pic_cnt += 1
#       cnt = 0
#       Picture(i,j)
#       area.append(cnt)
# print(pic_cnt)
# if area:
#   print(max(area))
# else:
#   print(0)


#while로 풀기
h, w = map(int,input().split())
graph = [[0]*w for _ in range(h)]
area = []
stack=[]
pic_cnt = 0
for i in range(h):
  graph[i] = list(map(int,input().split()))

for i in range(w):
  for j in range(h):
    if graph[j][i] == 1:
      stack.append((i,j))
      cnt = 0
      while stack:
        dx = [-1, 0, 0, 1]     # 4방 탐색
        dy = [0, 1, -1, 0]
        (x,y) = stack.pop()
        if graph[y][x] == 1:   # 1이면 4방 탐색 시작
          cnt += 1
          graph[y][x] = 0      # 방문시 0으로 변환
          for k in range(4):
            _x = x + dx[k]
            _y = y + dy[k]
            if 0 <= _x < w and 0 <= _y < h:  # 범위 조건
              if graph[_y][_x] == 1:
                stack.append((_x,_y))
      pic_cnt += 1
      area.append(cnt)
print(pic_cnt)
if area:
  print(max(area))
else:
  print(0)