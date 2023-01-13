2,1,1,0


[1,2,3,4]
[2,3,1,4]
[3,2,1,4]
[2,1,4,3]
[4,2,1,3]

# 1부터 차례대로 위치를 정하는데 정하고 나서는 없는 인덱스 처럼 취급하기

n = int(input())
inform = list(map(int,input().split()))
answer = ['#']*n
for num in range(1,n+1):
    print(answer)
    left_big = inform[num - 1]
    cnt = 0
    for i in range(n):
        to_find = answer[i]
        if to_find == '#':
            if cnt == left_big:
                answer[i] = num
                break
            else:
                cnt += 1
print(*answer)