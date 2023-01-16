INF = int(200)
n, m, r = map(int,input().split())
graph = [[INF] * (n + 1) for _ in range(n+1)]
items = list(map(int,input().split()))
answer = []

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    graph[a][a] = 0

# 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(r):
    s, e, d = map(int,input().split())
    graph[s][e] = d
    graph[e][s] = d

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 시작 노드별 최대 파밍 저장
for start_node in range(1,n+1):
    pharming = 0
    for i in range(1,n+1):
        distance = graph[start_node][i]
        if distance <= m:
            pharming += items[i-1]
    answer.append(pharming)
print(max(answer))