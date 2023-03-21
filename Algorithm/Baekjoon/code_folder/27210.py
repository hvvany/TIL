# 시작부터 특정 위치까지의 합을 담아놓고 구간을 정하면 큰거 - 작은거 구현하면 된다...
import sys
input = sys.stdin.readline

n = int(input())
inform_lst = list(map(int,input().split()))
memory = [n,-n]  # [최소값, 최대값]
print(f'inform_lst : {inform_lst}')
lst = []
깨달음 = 0
for i in range(n):
    if inform_lst[i] == 1:
        깨달음 += 1
    else:
        깨달음 -= 1
    if 깨달음 < memory[0]:
        memory[0] = 깨달음
    if 깨달음 > memory[1]:
        memory[1] = 깨달음
    lst.append(깨달음)

print(f'sum_lst : {lst}')
if memory[0] > 0:
    memory[0] = 0
if memory[1] < 0:
    memory[1] = 0
print(memory[1] - memory[0])