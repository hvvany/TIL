n, m = map(int,input().split())
dic = dict()
lst = [0]
for i in range(n):
  name = input()
  dic[name] = i + 1
  lst.append(name)
for _ in range(m):
  search = input()
  if search in dic:
    print(dic[search])
  else:
    print(lst[int(search)])
