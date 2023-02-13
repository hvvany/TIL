INF = int(10e6)

def binary(arr,start,end,target):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    if end < 0:
        end = 0
    if start >= n :
        start = n - 1
    if abs(arr[start] - target) > abs(arr[end] - target):
        return end
    else:
        return start

n = int(input())
lst = list(map(int,input().split()))
answer_val = INF
answer = []
lst.sort()
for i in range(n):
    second = binary(lst,0,n-1,-lst[i])
    dif = abs(lst[i] + lst[second])
    if dif < answer_val:
        answer_val = dif
        answer = [i,second]
        print(f'answer :{answer}')
if answer[0] == answer[1]:
    if answer[0] == 0:
        result = (lst[0],lst[1])
    else:
        result = (lst[-2],lst[-1])
else:
    result = (lst[answer[0]],lst[answer[1]])
print(*(sorted(result)))