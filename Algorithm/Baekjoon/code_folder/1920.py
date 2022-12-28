n = int(input())
num_lst = list(map(int,input().split()))
m = int(input())
check_lst = list(map(int,input().split()))
num_lst.sort()

def binary(array, target, start, end):
    check_idx = 0

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for num in check_lst:
    print(binary(num_lst, num, 0, len(num_lst)-1))