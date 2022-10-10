# import math


# t = int(input())
# for _ in range(t):
#   x1, y1, r1, x2, y2, r2 = map(int,input().split())
#   if x1 == x2 and y1 == y2:
#     if r1 == r2:
#       print(-1)
#     else:
#       print(0)
#   else:
#     between = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    
#     if between + r1 < r2 or between + r2 < r1:
#       print(0)
#     elif between + r1 == r2 or between + r2 == r1:
#       print(1)
#     elif between < r1 + r2:
#       print(2)
#     elif between == r1 + r2:
#       print(1)
#     else:
#       print(0)

