import math

n = int(input())
q = math.ceil(math.sqrt(n))

if q >= 0:
    print(q)
else:
    print(0)