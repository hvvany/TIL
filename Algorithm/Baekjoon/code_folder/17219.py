n, m = map(int,input().split())
dic = dict()
for _ in range(n):
  lst = input().split()
  dic[lst[0]] = lst[1]
for _ in range(m):
  lst = input().split()
  print(dic[lst[0]])