w  = []
k = []
for _ in range(10):
    w.append(int(input()))
for _ in range(10):
    k.append(int(input()))
w.sort()
k.sort()
print(sum(w[-3:]), sum(k[-3:]))