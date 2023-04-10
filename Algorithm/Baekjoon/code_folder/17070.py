import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

answer = 0
def dfs(i,j,dir):
  global answer
  if (i,j) == (n-1,n-1):
    answer += 1
    return
  
  if dir == '가로' or dir == '대각선':
    if j + 1 < n and graph[i][j+1] == 0:
      dfs(i,j+1,'가로')
  
  if dir == '세로' or dir == '대각선':
    if i + 1 < n and graph[i+1][j] == 0:
      dfs(i+1,j,'세로')

  if dir == '가로' or dir == '세로' or dir == '대각선':
    if j + 1 < n and i + 1 < n and graph[i][j+1] == graph[i+1][j] == graph[i+1][j+1] == 0:
      dfs(i+1,j+1,'대각선')
      
dfs(0,1,'가로')
print(answer)