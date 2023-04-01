from copy import deepcopy
import sys
input = sys.stdin.readline

move_lst = list(map(int,input().split()))
dist = [
  [1, 2, 2, 2, 2],
  [2, 1, 3, 4, 3],
  [2, 3, 1, 3, 4],
  [2, 4, 3, 1, 3],
  [2, 3, 4, 3, 1]]
INF = 10**9
# foot_lst = [(0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]
dp_one = [[INF]*5 for _ in range(5)]
dp_two = [[INF]*5 for _ in range(5)]
# 초기값 입력해주기
dp_one[0][move_lst[0]] = dp_one[move_lst[0]][0] = 2
for idx in range(1,len(move_lst)-1):
  move_num = move_lst[idx]
  for i in range(4):
    for j in range(i+1,5):
      if dp_one[i][j] != INF:
        dp_two[i][move_num] = dp_two[move_num][i] = min(dp_two[move_num][i], dp_one[i][j] + dist[move_num][j])
        dp_two[move_num][j] = dp_two[j][move_num] = min(dp_two[j][move_num], dp_one[i][j] + dist[move_num][i])
  dp_one = deepcopy(dp_two)
  dp_two = [[INF]*5 for _ in range(5)]
answer = 10**9
for i in range(4):
  for j in range(i+1,5):
    if dp_one[i][j] != INF and dp_one[i][j] < answer:
      answer = dp_one[i][j]
# print(dp_one)
print(answer)
dp_one[0][-1] = 2
print(dp_one)