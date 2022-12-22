from collections import deque
import sys
# input = sys.stdin.readline

deq = deque()
n = int(input())
for _ in range(n):
    입력 = input()
    if 입력[0:4] == 'push':
        order, num = 입력.split()
        deq.append(num)
    elif 입력 == 'pop':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif 입력 == 'size':
        print(len(deq))
    elif 입력 == 'empty':
        if deq:
            print(0)
        else:
            print(1)
    elif 입력 == 'front':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif 입력 == 'back':
        if deq:
            print(deq[-1])
        else:
            print(-1)