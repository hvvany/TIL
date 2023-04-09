import sys, heapq
input = sys.stdin.readline

# 최소비용 구하기
N = int(input())
M = int(input())
INF = 10**6

# 최단거리 저장 배열
distance = [INF]*(N+1)
visited = [False]*(N+1)
# 인접 행렬
graph = [[] for _ in range(M+1)]
for _ in range(M):
  s,e,k = map(int,input().split())
  graph[s].append((e,k))
  
# 시작, 도착 노드 정보
start, dest = map(int,input().split())

# 가장 가까운 노드 반환 함수
def NextNode():
  min_val = INF
  idx = 0
  for i in range(1,N+1):
    if distance[i] < min_val and not visited[i]:
      min_val = distance[i]
      idx = i
  return idx

def dijkstra(start):
  distance[start] = 0
  visited[start] = True
  for info in graph[start]:
    distance[info[0]] = info[1]
  
  for _ in range(N-1):
    # print(distance)
    # print(f'visited : {visited}')
    now = NextNode()
    visited[now] = True
    for inf in graph[now]:
      if visited[inf[0]] == False:
        distance[inf[0]] = min(distance[inf[0]],distance[now]+inf[1])
      
dijkstra(start)
print(distance[dest])