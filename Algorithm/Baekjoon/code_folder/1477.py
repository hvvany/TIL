# n, m, l = map(int,input().split())
# huge_lst = list(map(int,input().split()))
# huge_lst.sort()
# # 이분 탐색을...전체 돌면서..?
# def binary(lst,d_s,d_e,target_cnt):
#     global n,l
#     while d_s < d_e:
#         test_lst = []
#         now = 0
#         idx = 0
#         cnt = 0
#         print("............")
#         while True:
#         # cnt 계산하는 반복문
#             d_m = (d_s + d_e) // 2
#             if idx == n:
#                 print(f'd_m : {d_m}')
#                 if now > l:
#                     break
#                 else:
#                     print("?????????????")
#                     test_lst.append(now)
#                     now += d_m
#                     cnt += 1
#             elif now < lst[idx] - d_m:  # 기존 휴게소와 겹치면 안되므로 같은 경우는 패스
#                 test_lst.append(now)
#                 now += d_m
#                 cnt += 1
#             elif now >= lst[idx] - d_m:
#                 now = lst[idx] + d_m
#                 idx += 1
#         if lst[0] != 0:
#             cnt -= 1
#         if cnt == target_cnt:

#         elif cnt > target_cnt:
#             d_s = d_m + 1
#         else:
#             d_e = d_m - 1
#     print(f'test_lst : {test_lst}')
#     return d_m

# # 기준 거리를 정해서 줄여가면서 가장 많이 들어가는 수 정하기
# # 중간에 기존 휴게소 만나면... 그 휴게소에서 기준 거리 더했을 때 뒤에 거리 괜찮으면 추가
# # -> 기준 거리 * 2 했을 때 크기 안되면 지을 수 없다. 그다음 구간 넘어가기
# print(binary(huge_lst,0,l//n + 1,m))




# n, m, l = map(int,input().split())
# huge_lst = list(map(int,input().split()))
# huge_lst.sort()
# # 이분 탐색을...전체 돌면서..?
# def binary(lst,d_s,d_e,target_cnt):
#     global n,l
#     while d_s <= d_e:
#         now = 1
#         idx = 0
#         cnt = 0
#         test = []
#         while True:
#         # cnt 계산하는 반복문
#             d_m = (d_s + d_e) // 2
#             if idx == n:
#                 if now >= l:
#                     break
#                 else:
#                     test.append(now)
#                     now += d_m
#                     cnt += 1
#             elif now < lst[idx]:  # 기존 휴게소와 겹치면 안되므로 같은 경우는 패스
#                 test.append(now)
#                 now += d_m
#                 cnt += 1
#             elif now >= lst[idx]:
#                 idx += 1
#         print(f'd_m {d_m}, cnt : {cnt}')
#         print(huge_lst)
#         print(test)

#         # if lst[0] == 0:
#         #     cnt -= 1
#         if cnt >= target_cnt:
#             d_s = d_m + 1
#         else:
#             d_e = d_m - 1
#     return d_m

# 기준 거리를 정해서 줄여가면서 가장 많이 들어가는 수 정하기
# 중간에 기존 휴게소 만나면... 그 휴게소에서 기준 거리 더했을 때 뒤에 거리 괜찮으면 추가
# -> 기준 거리 * 2 했을 때 크기 안되면 지을 수 없다. 그다음 구간 넘어가기
# print(binary(huge_lst,0,l//n + 1,m))






# 휴게소 세우기
N, M, L = map(int, input().split())
arr = [0]+list(map(int, input().split()))+[L]
arr.sort()

start, end = 1, L-1
result = 0
while start <= end:
    count = 0
    mid = (start+end) // 2
    for i in range(1, len(arr)):
        # 현재 거리 중 mid보다 큰 거리를 찾아서
        if arr[i]-arr[i-1] > mid:
            # 나눈 만큼 휴게소를 설치 (현재 설치 돼있는 구역은 제외해야해서 -1)
            count += (arr[i]-arr[i-1]-1)//mid
    if count > M:
        start = mid+1
    else:
        end = mid-1
        result = mid
print(result)