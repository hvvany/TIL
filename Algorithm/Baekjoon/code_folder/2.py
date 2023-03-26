# 팔
# https://www.acmicpc.net/problem/1105

l, r = map(str,input().split())
ll = len(l)
rl = len(r)
l = l.zfill(max(ll,rl))
r = r.zfill(max(ll,rl))
answer = 0
for idx in range(max(ll,rl)):
  if l[idx] != r[idx]:
    break
  if l[idx] == r[idx] == '8':
    answer += 1
print(answer)