n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [False]*n
answer = 0

def dfs(node):
    print(f'visited : {visited}')
    global depth
    # if visited[node] == False:
    #     visited[node] = True
    print(f'num :{node}')
    # depth += 1
    for idx in range(n):
        if graph[node][idx] == 'Y':
            if visited[idx] == False:
                visited[idx] = True
                depth += 1
                dfs(idx)

for i in range(n):
    depth = 0
    dfs(i)
    print(f'depth{i} : {depth}')
    if answer < depth:
        answer = depth
print(answer - 1)