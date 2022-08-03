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
num_lst = list(map(int,input().split()))
num_before = 0
for i in range(n):
    num = num_lst[i] 
    if i == n-1:
        print(-1)
    elif num != num_lst[i+1]:
        j = i + 2
        print(j,end=' ')
    else:
        idx = i
        breaker = False
        if num == num_before:
            print(j_before,end=' ')
            continue
        while num_lst[idx] == num:
            j = idx + 2
            idx += 1
            if idx == n:
                print(-1,end=' ')
                breaker = True
                break
        if breaker == True:
            continue
        num_before = num
        j_before = j
        print(j,end=' ')