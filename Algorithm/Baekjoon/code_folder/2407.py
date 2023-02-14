def combi(n,m):
    if m == 0 or m == n:
        return 1
    elif graph[n][m] != 0:
        return graph[n][m]
    else:
        graph[n][m] = combi(n-1,m-1) + combi(n-1,m)
        return graph[n][m]

n, m = map(int,input().split())
graph = [[0]*(m+1) for _ in range(n+1)]
print(combi(n,m))