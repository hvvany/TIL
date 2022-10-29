# n, k = map(int,input().split())
# answer = []
# num_lst = list(range(1,n+1))
# visited_idx = set()
# cnt = 0
# number = k
# while num_lst:
#     print(num_lst)
#     idx = (number - 1) % n
#     print(f'idx:"{idx}')
#     if idx in visited_idx:
#         print("---")
#         number += 1
#     else:
#         visited_idx.add(idx)
#         answer.append(num_lst[idx])
#         number += k
#         cnt += 1
#         num_lst[idx] = 0

#     if cnt == n:
#         break

#     print(f'number : {number}, idx : {idx}')
# print(answer)
# print(visited_idx)


seting = []
seting.append(2)
seting.append(1)
seting.append(5)
if 2 in seting:
    print('yes')
else:
    print('no')