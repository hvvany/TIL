n, m = map(int,input().split())
lst_1 = []
lst_2 = []
for _ in range(m):
  six, one = map(int,input().split())
  lst_1.append(min(six*(n//6),one*6*(n//6)))
  lst_2.append(min(six,one*(n%6)))
print(min(lst_1) + min(lst_2))