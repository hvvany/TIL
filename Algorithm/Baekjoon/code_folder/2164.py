from collections import deque

n = int(input())
lst = deque(range(1,n+1))
cnt = 0
card = 0
while lst:
  cnt+=1
  card = lst.popleft()
  if cnt % 2 == 0:
    lst.append(card)
print(card)