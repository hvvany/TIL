# n, k = map(int,input().split())
# caf_lst = list(map(int,input().split()))
# caf_lst.sort()
# graph = [[10**6]*(n+1) for _ in range(n+1)]
# for i in range(1,n+1):
#   for j in range(1,n+1):
#     graph[i][j] = min(graph[i-1][j], graph[i-1][j-1] + caf_lst[i-1])
# answer = -1
# for idx in range(n+1):
#   if graph[-1][idx] == k:
#     answer = idx
#     break
# print(graph)
# print(answer)

import sys

n, k = map(int, sys.stdin.readline().split())
coins = list(map(int, sys.stdin.readline().split()))

dp = [10**6] * (k + 1)
dp[0] = 0

for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

if dp[k] == 10**6:
    print("-1")
else:
    print(dp[k])
