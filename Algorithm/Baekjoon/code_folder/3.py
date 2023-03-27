# 에디터
# https://www.acmicpc.net/problem/1406

from collections import deque
import sys
input = sys.stdin.readline


front = deque(list(input().rstrip()))
back = deque()
m = int(input().rstrip())
for _ in range(m):
  order = input()
  if order[0] == 'L':
    if front:
      back.appendleft(front.pop())
  elif order[0] == 'D':
    if back:
      front.append(back.popleft())
  elif order[0] == 'B':
    if front:
      front.pop()
  elif order[0] == 'P':
    od,ch = order.split()
    for c in ch:
      front.append(c)
      
answer = ''.join(front) + ''.join(back)
print(answer)