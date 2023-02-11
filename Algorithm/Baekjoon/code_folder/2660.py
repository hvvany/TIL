INF = 10**6
n = int(input())
graph = [[INF]*(n) for _ in range(n)]

for i in range(n):
    graph[i][i] = 0 # 자기 자신 0

while True:
    a,b = map(int,input().split())
    if (a,b) == (-1,-1):
        break
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

king = INF
answer = []
for i in range(n):
    big = max(graph[i])
    if big < king:
        answer = [i+1]
        king = big
    elif big == king:
        answer.append(i+1)
print(graph)
print(king,len(answer))
print(*sorted(answer))