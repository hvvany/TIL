# 몫고 나머지 차이로 거리 계산
n1, n2 = map(int,input().split())
m1 = n1 // 4
l1 = n1 % 4
m2 = n2 // 4
l2 = n2 % 4
if n1 % 4 == 0:
    m1 = n1 // 4 - 1
    l1 = 4
if n2 % 4 == 0:
    m2 = n2 // 4 - 1
    l2 = 4
print(abs(m1-m2)+abs(l1-l2))