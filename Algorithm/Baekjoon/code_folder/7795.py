t = int(input())
lst_a = []
lst_b = []

def binary(arr, target, start, end):
    global cnt
    result = 0
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] > target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

for _ in range(t):
    a, b = map(int,input().split())
    lst_a = list(map(int,input().split()))
    lst_b = list(map(int,input().split()))
    lst_b.sort()

    cnt = 0
    for num in lst_a:
        cnt += binary(lst_b, num, 0, b - 1) + 1
    print(cnt)