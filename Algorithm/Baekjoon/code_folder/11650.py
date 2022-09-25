lst = []
t = int(input())
for _ in range(t):
  lst.append(tuple(map(int,input().split())))
new_lst = sorted(lst,key=lambda x:(x[1],x[0]))
for (x,y) in new_lst:
  print(x,y)