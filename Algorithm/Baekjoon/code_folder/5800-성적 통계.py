import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    gap = 0
    data_lst = list(map(int,input().split()))
    score_lst = data_lst[1:]
    score_lst.sort()
    for idx in range(data_lst[0]-1):
        if score_lst[idx+1] - score_lst[idx] > gap:
            gap = score_lst[idx+1] - score_lst[idx]

    print(f'Class {i+1}')
    print(f'Max {score_lst[-1]}, Min {score_lst[0]}, Largest gap {gap}')
