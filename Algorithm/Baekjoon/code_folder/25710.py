# from itertools import combinations
# import heapq
# import sys
# input = sys.stdin.readline

# n = int(input().rstrip())
# lst = list(map(int,input().split()))
# num_lst = []

# comb = list(combinations(lst,2))
# for num in comb:
#   pro = num[0]*num[1]
#   s = 0
#   for i in str(pro):
#     s += int(i)
#   heapq.heappush(num_lst,-s)

# print(-heapq.heappop(num_lst))


import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = list(map(int,input().split()))
num_lst = []

for i in range(len(lst)-1):
  for j in range(i+1,len(lst)):
    pro = lst[i]*lst[j]
    s = 0
    for k in str(pro):
      s += int(k)
    heapq.heappush(num_lst,-s)

print(-heapq.heappop(num_lst))