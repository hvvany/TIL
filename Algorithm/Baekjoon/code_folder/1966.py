from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int,input().split())
    lst = deque(map(int,input().split()))
    important_stack = sorted(lst,reverse=True)
    for i in range(n):
        lst.append((lst.popleft(),i))
    answer = 0
    breaker = False
    for num in important_stack:
        if breaker:
            break
        for i in range(len(lst)):
            if lst:
                left = lst.popleft()
            else:
                break
            if left[0] != num:
                lst.append(left)
            else:
                answer += 1
                if left[1] == m:
                    breaker = True
                break
    print(answer)