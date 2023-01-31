INF = 1e9

n, total = map(int,input().split())
node_set = {0,total}
for _ in range(n):
    s, e, l = map(int,input().split())
    node_set.add(s)
    node_set.add(e)
node_cnt = len(node_set)
graph = [[] for i in range(node_cnt+1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

