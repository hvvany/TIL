n = int(input())
pen_lst = list(map(int,input().split()))
k = int(input())
target_lst = list(map(int,input().split()))
graph = [[False]*40001 for _ in range(n+1)]
# 더하기 
for idx in range(1,n+1):
  pen = pen_lst[idx-1]
  graph[idx][pen] = True
  # print(f'pen : {pen}')
  for i in range(1,40001):
    if graph[idx-1][i] == True:
      graph[idx][i] = True
      if i + pen < 40001:
        graph[idx][i+pen] = True
# print(f'graph : {graph}')
# 빼기
for pen in pen_lst:
  for i in range(1,40001):
    if graph[-1][i] == True:
      if i - pen > 0:
        graph[-1][i-pen] = True
# print(f'graph2 : {graph}')

# print(graph[-1])
for target in target_lst:
  if graph[-1][target] == True:
    print('Y', end=' ')
  else:
    print('N', end=' ')