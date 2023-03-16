import sys

n, m = map(int,input().split())
graph = [[0]*(m+1)]
graph += [([0]+list(input())) for _ in range(n)]
check = ['W','B']
cnt = 0
for i in range(1,n+1):
    if m % 2 == 0:
        cnt += 1
    for j in range(1,m+1):
        if graph[i][j] != check[cnt % 2]:
            graph[i][j] = 1
        else:
            graph[i][j] = 0
        graph[i][j] += graph[i][j-1] + graph[i-1][j] - graph[i-1][j-1]
        cnt += 1
answer_min = sys.maxsize
answer_max = -sys.maxsize
for i in range(n+1-8):
    for j in range(m+1-8):
        num = graph[i+8][j+8] - graph[i][j+8] - graph[i+8][j] + graph[i][j]
        if num < answer_min:
            answer_min = num
        if num > answer_max:
            answer_max = num
print(min(answer_min, 64 - answer_max))