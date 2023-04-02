# 마법사 상어와 복제
import sys
input = sys.stdin.readline
# 기본 정보 저장해놓기 -> 복제 시 시간 단축 위해
M, S = map(int,input().split())
fish_memory = []
for _ in range(M):
  fish_memory.append(tuple(map(int,input().split())))
shark_memory = tuple(map(int,input().split()))
grid = [[[] for _ in range(5)] for _ in range(5)]
visited = [[False]*5 for _ in range(5)]
scent_memory = [[-100]*5 for _ in range(5)]
for fish in fish_memory:
  grid[fish[0]][fish[1]].append(fish[2])
after_fish_move_grid = [[[] for _ in range(5)] for _ in range(5)]

def fishMove(i,j,d):
  global now_turn, now_shark
  dx = [0,-1,-1,-1,0,1,1,1]
  dy = [-1,-1,0,1,1,1,0,-1]
  for idx in range(8): # d가 인덱스로는 현재 방향 다음 각도여서
    idx = d - 1 - idx
    nx = i + dx[idx]
    ny = j + dy[idx]
    if 1 <= nx < 5 and 1 <= ny < 5:
      if scent_memory[nx][ny] < now_turn - 2:
        if (nx,ny) != now_shark:
          if idx < 0:
            idx += 8
          after_fish_move_grid[nx][ny].append(idx+1)
          return
  after_fish_move_grid[i][j].append(d)

dx = [-1,0,1,0]
dy = [0,-1,0,1]
def sharkMove(i,j,eat_lst,dir_lst): # dir lst 길이로 깊이 판단
  global now_shark
  if len(dir_lst) == 3:
    eat_check = 0
    for inform in eat_lst:
      eat_check += len(inform[2])
    eat_memory_lst.append([eat_check,''.join(dir_lst),eat_lst,i,j])
    return
  for idx in range(4):
    nx = i + dx[idx]
    ny = j + dy[idx]
    if 1 <= nx < 5 and 1 <= ny < 5:
      # scent_inform = scent_memory[nx][ny]
      if not visited[nx][ny]:
        visited[nx][ny] = True
        if after_fish_move_grid[nx][ny]:
          # if scent_memory[nx][ny] < now_turn:
          #   scent_memory[nx][ny] = now_turn
          sharkMove(nx,ny,eat_lst + [[nx,ny,after_fish_move_grid[nx][ny]]],dir_lst + [str(idx + 1)])
        else:
          sharkMove(nx,ny,eat_lst + [[nx,ny,[]]],dir_lst + [str(idx + 1)])
        visited[nx][ny] = False
        # scent_memory[nx][ny] = scent_inform
      else:
        sharkMove(nx,ny,eat_lst + [[nx,ny,[]]],dir_lst + [str(idx + 1)])

answer = 0
now_shark = (shark_memory[0],shark_memory[1])
for now_turn in range(1,S+1):
  visited = [[False]*5 for _ in range(5)]
  eat_cnt = 0
  cnt_ = 0
  # print(f'\n-------turn {now_turn} --------')
  # print(f'now_shark : {now_shark}')
  # pprint(f'{grid}')
  # print(f'\n before_fish_move : {grid}')
  for i in range(5):
    for j in range(5):
      cnt_ += len(grid[i][j])
      if grid[i][j]:
        for di in grid[i][j]:
          fishMove(i,j,di)
  # print(f'scent : {scent_memory}')
  # print(f'\n after_fish_move : {after_fish_move_grid}')
  # print(f'before_cnt : {cnt_}')
  eat_memory_lst = []
  visited[now_shark[0]][now_shark[1]] = True
  sharkMove(now_shark[0],now_shark[1],[],[])
  eat_memory_lst.sort(key=lambda x:(-x[0],x[1]))
  now_shark = (eat_memory_lst[0][3],eat_memory_lst[0][4])
  for fish in eat_memory_lst[0][2]:
    after_fish_move_grid[fish[0]][fish[1]] = []
    if fish[2]:
      scent_memory[fish[0]][fish[1]] = now_turn
  # pprint(eat_memory_lst)
  # pprint(f'grid : \n {grid}')
  # print(f'sssss11111 \n {grid} \n ------- \n {after_fish_move_grid}')
  for i in range(5):
    for j in range(5):
      grid[i][j] += after_fish_move_grid[i][j]
      # cnt_ += len(after_fish_move_grid[i][j])
  # grid = copy.deepcopy(after_fish_move_grid)
  after_fish_move_grid = [[[] for _ in range(5)] for _ in range(5)]
  if eat_memory_lst:
    eat_cnt += eat_memory_lst[0][0]
  # print(f'eat_cnt : {eat_cnt}')
  answer = cnt_*2 - eat_cnt
print(answer)