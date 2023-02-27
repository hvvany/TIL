from collections import deque
import sys
input = sys.stdin.readline

def bfs(a,b):
    global answer
    visited = set()
    q = deque([(a,b)])
    while q:
        now,cnt = q.popleft()
        if now >= 100:
            if answer > cnt:
                answer = cnt
            return
        if now in go and now not in visited:
            visited.add(now)
            visited.add(go[now])
            q.append((go[now],cnt))
        else:
            for num in range(1,7):
                if now + num not in visited:
                    visited.add(now)
                    q.append((now+num,cnt + 1))

N, M = map(int,input().split())
go = dict()
for _ in range(N+M):
    f, t = map(int,input().split())
    go[f] = t
answer = 100
bfs(1,0)
print(answer)