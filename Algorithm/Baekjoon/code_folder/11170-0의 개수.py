import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    cnt = 0
    start, finish = map(int,input().split())
    for number in range(start, finish+1):
        cnt += str(number).count('0')
    print(cnt)