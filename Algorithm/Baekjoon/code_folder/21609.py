# 상어 중학교
n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
score = 0

# dfs로 방문하며 정보 획득
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def dfs(i,j,color):
  global block_cnt, rainbow_cnt, grp_row, grp_col
  visited[i][j] = True
  if i < grp_row:
    grp_row = i
    grp_col = j
  elif i == grp_row and j < grp_col:
    grp_row = i
    grp_col = j
  if graph[i][j] == 0:
    rainbow_cnt += 1
  elif graph[i][j] > 0:
    block_cnt += 1
  for idx in range(4):
    nx = i + dx[idx]
    ny = j + dy[idx]
    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
      if graph[nx][ny] == color or graph[nx][ny] == 0:
        dfs(nx,ny,color)

# auto play 구현 시작점
while True:
  # 시간 줄이기 위해 -1 ~ m 까지 번호를 키로 가지는 좌표정보 넣기
  inform_dic = {-1:[],0:[],1:[],2:[],3:[],4:[],5:[]}
  for i in range(n):
    for j in range(n):
      inform_dic[graph[i][j]].append((i,j))
  # 최대 넓이의 그룹 뽑기
  # 그룹 저장할 리스트 [블록개수,무지개수,기준행,기준열] -> sort
  group_lst = []
  
  # 그룹 컬러 선택
  for color in range(1,m+1):
    # 그래프에서 해당 컬러이면 최대 넓이 계산 _ 0은 방문상관 x  ____ 혹시 시간 초과 나면 줄일 수 있는 부분
    visited = [[False]*n for _ in range(n)]
    for coor in inform_dic[color]:
      (i, j) = coor
      if not visited[i][j] and graph[i][j] == color:
        block_cnt, rainbow_cnt, grp_row, grp_col = 0, 0, 21, 21
        dfs(i,j,color)
        group_lst.append((block_cnt, rainbow_cnt, grp_row, grp_col, color))
        # 0은 방문 초기화하기
        for zero in inform_dic[0]:
          (x, y) = zero
          visited[x][y] = False
  if len(group_lst) < 2:
    break
  group_lst.sort(reverse=True)
  score += (group_lst[0][0] + group_lst[0][1])**2

  # 1차 중력 작용
  
  
  
  
  
  
  
print(score)