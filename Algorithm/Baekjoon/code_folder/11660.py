# n, m = map(int,input().split())
# graph = [list(map(int,input().split())) for _ in range(n)]
# for _ in range(m):
#     answer = 0
#     x1, y1, x2, y2 = map(int,input().split())
#     for j in range(y1-1,y2):
#         answer += sum(graph[j][x1-1:x2])
#     print(answer)


# dp로 풀어야 하는군...
# 해당하는 좌표까지 원점에서의 합을 저장해놓으면 양 꼭짓점에서 큰 값에서 작은값 빼주면 될거 같은데...

n, m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
memory = [[] for _ in range(n)]

for _ in range(m):
    answer = 0
    x1, y1, x2, y2 = map(int,input().split())
    for j in range(y1-1,y2):
        answer += sum(graph[j][x1-1:x2])
    print(answer)