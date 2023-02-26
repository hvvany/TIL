import sys
input = sys.stdin.readline

def solution():
    V, E = map(int,input().split())
    adjList = [dict() for _ in range(V+1)]
    INF = 10**6
    distance = [INF]*(V+1)
    start = int(input())
    for _ in range(E):
        f,t,w = map(int,input().split())
        adjList[f][t]= w
    for num in adjList[start]:
        distance[num] = adjList[start][num]
    adjList[start][start] = 0
    for i in range(1,V+1):
        for j in range(1,V+1):
            if j not in adjList[i]:
                adjList[i][j] = INF
            if j not in adjList[start]:
                adjList[start][j] = INF
            distance[j] = min(distance[j],min(distance[i] + adjList[i][j], adjList[start][j]))

    for i in range(1,V+1):
        if distance[i] <= 10:
            print(distance[i])
        else:
            print('INF')
solution()