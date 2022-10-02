# n, p, q = map(int,input().split())
# a = [1,2] + [0]*n

# def Inf(k):
#   global p
#   global q
#   global a
#   i = 2
#   while i <= k:
#     a[i] = a[i//p] + a[i//q]
#     i += 1
#   return a[k]

# print(Inf(n))

# n, p, q = map(int,input().split())
# a = [1,2] + [0]*(n//min(p,q))

# def Inf(k):
#   global p
#   global q
#   global a
#   i = 2
#   while i < k:
#     a[i] = a[i//p] + a[i//q]
#     i += 1
#   return a[k]

# print(Inf(n))



import sys
input = sys.stdin.readline

n, p, q = map(int,input().split())

dic = {0:1,1:2}

def Inf(k):
  if k in dic:
    return dic[k]
  else:
    dic[k] = Inf(k//p) + Inf(k//q)
    return dic[k]

print(Inf(n))