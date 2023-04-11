def makeSet():
  for i in range(n):
    parents[i] = i

def findSet(a):
  if parents[a] == a:
    return a
  parents[a] = findSet(parents[a])
  return parents[a]

def union(a,b):
  aRoot = findSet(a)
  bRoot = findSet(b)
  if aRoot == bRoot:
    return False
  parents[bRoot] = aRoot
  return True
  
n, m, k = map(int,input().split())
parents = [0]*(n+1)
friend_ratio = list(map(int,input().split()))
makeSet()

for i in range(m):
  a, b = map(int,input().split())
  union(a,b)

group_min_cost = dict()
for i in range(1,n+1):
  group = findSet(i)
  if group in group_min_cost:
    if group_min_cost[group] > friend_ratio[i-1]:
      group_min_cost[group] = friend_ratio[i-1]
  else:
    group_min_cost[group] = friend_ratio[i-1]
    
answer = sum(group_min_cost.values())
if answer > k:
  print('Oh no')
else:
  print(answer)