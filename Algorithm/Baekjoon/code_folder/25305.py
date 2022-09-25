n,m = map(int,input().split())
lst = list(map(int,input().split()))
print(sorted(lst,reverse=True)[m-1])