import sys
input = sys.stdin.readline

def binary(arr, target, start, end):
        global cnt
        while start <= end:
            mid = (start + end) // 2
            if target == arr[mid]:
                cnt += 1
                return
            elif target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1

while True:
    n, m = map(int,input().split())
    if n == 0 and m == 0:
        break
    sg_lst = []
    sy_lst = []
    cnt = 0
    for _ in range(n):
        sg_lst.append(int(input()))
    for _ in range(m):
        sy_lst.append(int(input()))

    for num in sg_lst:
        binary(sy_lst,num,0,m-1)
    print(cnt)