import sys
input = sys.stdin.readline

def binary(lst, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return start

n, m = map(int,input().split())
wifi_lst = []
for i in range(n):
    wifi_lst.append(int(input()))
wifi_lst.sort()
wifi_distance = ((wifi_lst[-1] - wifi_lst[0]) // (m-1)) + 1
in_progress = True 
while True:
    print("------------")
    cnt = 0
    num = wifi_lst[0]
    for i in range(m-1):
        print(f'num : {num}')
        print(f'num _ distance : {num + wifi_distance}')
        if num + wifi_distance > wifi_lst[-1]:
            break
        num = wifi_lst[binary(wifi_lst,1,n-1,num + wifi_distance)]
    else:
        print(wifi_distance)
        break
    wifi_distance -= 1