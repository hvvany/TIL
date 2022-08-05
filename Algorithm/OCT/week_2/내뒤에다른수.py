# import sys
# input = sys.stdin.readline

# n = int(input())
# num_lst = list(map(int,input().split()))

# for i in range(n):
#     num = num_lst[i]
#     if i == n-1:
#         print(-1)
#     elif num != num_lst[i+1]:
#         j = i + 2
#         print(j,end=' ')
#     else:
#         idx = i
#         breaker = False
#         while num_lst[idx] == num:
#             j = idx + 2
#             idx += 1
#             if idx == n:
#                 print(-1,end=' ')
#                 breaker = True
#                 break
#         if breaker == True:
#             continue
#         print(j,end=' ')






import sys
input = sys.stdin.readline

n = int(input())
num_lst = list(map(int,input().split()))  # 수열 입력

num_before = 0
j_before = 0
for i in range(n):
    num = num_lst[i]    # 수열에 i인덱스 숫자 num
    if i == n-1:        # i 가 마지막 인덱스이면 -1
        print(-1)
    elif num != num_lst[i+1]:  # 바로 다음 숫자와 다르면
        j = i + 2              # 다른 그 숫자의 위치번호(인덱스+1) 출력
        print(j,end=' ')       
    else:                  
        idx = i
        breaker = False
        if num == num_before:         # 이전 num값과 같으면
            print(j_before,end=' ')   # 이전 j값 출력
            continue
        while num_lst[idx] == num:    # 인덱스를 현재 인덱스에서 1추가해보며 비교(다르면 종료)
            j = idx + 2               # j는 다른 숫자 나올때 까지 다른 숫자 위치번호(인덱스 + 1) 최신화
            idx += 1
            if idx == n:              # 반복문 돌다가 마지막 인덱스 접근하면 반복문 탈출
                print(-1,end=' ')
                breaker = True
                break

        if breaker == True:           # 아래에 print(j)를 생략하기 위해 브레이커 연동
            continue
        
        print(j,end=' ')
    num_before = num
    j_before = j