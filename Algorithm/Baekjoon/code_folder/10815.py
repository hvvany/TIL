n = int(input())
lst_1 = list(map(int,input().split()))
m = int(input())
lst_2 = list(map(int,input().split()))
for num in lst_2:
  if num in lst_1:
    print(1,end=' ')
  else:
    print(0,end=' ')