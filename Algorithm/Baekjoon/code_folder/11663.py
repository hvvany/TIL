import sys
input = sys.stdin.readline

n, m = map(int,input().split())
num_lst = list(map(int,input().split()))
num_lst.sort()
num_set = set(num_lst)

def binary(lst, s, e, target, status):
    mid = 0
    while s <= e:
        mid = (s + e)//2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            e = mid - 1
        else:
            s = mid + 1
    if status == 'start':
        return s
    else:
        return e

for i in range(len(num_lst)):
    contain = False
    answer = 0
    start, end = map(int,input().split())
    start_num = binary(num_lst,0,n-1,start,'start')
    end_num = binary(num_lst,0,n-1,end,'end')
    answer = end_num - start_num
    print(f'start : {start_num} end : {end_num}')
    print(answer + 1)