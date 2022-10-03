import heapq

lst = []

n = int(input())
for _ in range(n):
  inform = input()
  if inform == '0':
    if lst:
      print(-heapq.heappop(lst))
    else:
      print(-1)
  else:
    base = inform.split()
    for num in base[1:]:
      heapq.heappush(lst,-int(num))